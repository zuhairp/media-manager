package main

import (
	"encoding/binary"
	"fmt"
	"log"
	"net"
	"sync"
	"time"

	"github.com/golang/protobuf/proto"

	"github.com/pkg/errors"

	"github.com/zuhairp/media-manager/goprotos"
)

func writer(
	client net.Conn,
	output chan []byte,
	cancel chan bool,
	wg *sync.WaitGroup) {

	defer wg.Done()
	// Reusable buffer for fixed-size metadata
	metadataBytes := make([]byte, 2)

	for {
		select {
		case data := <-output:
			binary.BigEndian.PutUint16(metadataBytes, uint16(len(data)))
			_, err := client.Write(metadataBytes)
			if err != nil {
				// client probably disconnected, let's bail
				return
			}

			_, err = client.Write(data)
			if err != nil {
				// client probably disconnected, let's bail
				return
			}

		case <-cancel:
			// Received a signal on the cancel channel, let's bail
			return
		}
	}
}

func reader(
	client net.Conn,
	output chan []byte,
	cancel chan bool,
	wg *sync.WaitGroup) {
	defer wg.Done()

	// Reusable buffer for fixed-size metadata
	metadataBytes := make([]byte, 2)

	for {
		bytesRead, err := client.Read(metadataBytes)
		if bytesRead < len(metadataBytes) || err != nil {
			// Probably received EOF, so shut everything down
			if err != nil && err.Error() != "EOF" {
				log.Printf("ERROR: %q", err.Error())
			}
			select {
			case cancel <- true:
			case <-time.After(time.Second * 10):
				log.Printf("ERROR: Cancel timed out")
			}

			return
		}

		messageSize := binary.BigEndian.Uint16(metadataBytes)
		messageBytes := make([]byte, messageSize)

		bytesRead, err = client.Read(messageBytes)
		if bytesRead < len(metadataBytes) || err != nil {
			// Probably received EOF, so shut everything down
			if err != nil && err.Error() != "EOF" {
				log.Printf("ERROR: %q", err.Error())
			}
			select {
			case cancel <- true:
			case <-time.After(time.Second * 10):
				log.Printf("ERROR: Cancel timed out")
			}
			return
		}

		message := &media_manager.Request{}
		err = proto.Unmarshal(messageBytes, message)
		if err != nil {
			log.Printf("ERROR: %q", err.Error())
		}

		go HandleMessage(message, output)
	}
}

func handleRequest(client net.Conn) {
	addr := client.RemoteAddr()
	log.Printf("New connection from %q", addr.String())

	output := make(chan []byte)
	cancel := make(chan bool)

	var wg sync.WaitGroup
	wg.Add(2)
	go reader(client, output, cancel, &wg)
	go writer(client, output, cancel, &wg)

	wg.Wait()

	log.Printf("Disconected %q", addr.String())
}

func server(port int) error {
	addr := fmt.Sprintf("0.0.0.0:%d", port)
	listener, err := net.Listen("tcp", addr)
	if err != nil {
		return errors.Wrap(err, "Failed to start server")
	}

	defer listener.Close()
	log.Printf("Listening on %q", listener.Addr().String())
	for {
		conn, err := listener.Accept()
		if err != nil {
			return errors.Wrap(err, "Failed to accept client")
		}

		go handleRequest(conn)
	}

}

func main() {
	err := server(4896)
	if err != nil {
		fmt.Printf("FATAL: %+v\n", err)
	}
}

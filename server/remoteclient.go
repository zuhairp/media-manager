package main

import (
	"encoding/binary"
	"net"
	"os"

	"github.com/golang/protobuf/proto"
	"github.com/pkg/errors"

	"github.com/zuhairp/media-manager/goprotos"
)

func getRemoteConn() (net.Conn, error) {
	servAddr, exists := os.LookupEnv("REMOTE_SERVER_ADDR")
	if !exists {
		servAddr = "localhost:3296"
	}

	tcpAddr, err := net.ResolveTCPAddr("tcp", servAddr)
	if err != nil {
		return nil, errors.Wrapf(err, "failed to resolve server address %q", servAddr)
	}

	return net.DialTCP("tcp", nil, tcpAddr)
}

func writeMessageFrame(conn net.Conn, data []byte) error {
	size := uint16(len(data))

	metadata := make([]byte, 2)
	binary.BigEndian.PutUint16(metadata, size)

	if _, err := conn.Write(metadata); err != nil {
		return err
	}

	_, err := conn.Write(data)
	return err
}

func readMessageFrame(conn net.Conn) (*media_manager.Response, error) {
	responseSizeBytes := make([]byte, 2)
	if _, err := conn.Read(responseSizeBytes); err != nil {
		return nil, err
	}

	responseSize := binary.BigEndian.Uint16(responseSizeBytes)
	responseData := make([]byte, responseSize)

	if _, err := conn.Read(responseData); err != nil {
		return nil, err
	}

	response := &media_manager.Response{}
	if err := proto.Unmarshal(responseData, response); err != nil {
		return nil, err
	}

	return response, nil
}

func ListFiles(location media_manager.Location) ([]string, error) {

	conn, err := getRemoteConn()

	if err != nil {
		return nil, err
	}

	defer conn.Close()

	request := &media_manager.Request{
		Type: &media_manager.Request_Fileslist{
			Fileslist: &media_manager.FilesListRequest{
				Location: location,
			},
		},
	}

	data, err := proto.Marshal(request)
	if err != nil {
		return nil, errors.Wrap(err, "Failed to serialize request")
	}

	writeMessageFrame(conn, data)
	response, err := readMessageFrame(conn)
	if err != nil {
		return nil, err
	}

	filenames := response.GetFileslist().Filenames

	return filenames, nil
}

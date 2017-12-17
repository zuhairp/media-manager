package main

import (
	"log"
	"time"

	"github.com/golang/protobuf/proto"

	"github.com/zuhairp/media-manager/goprotos"
)

func HandleMessage(message *media_manager.Request, output chan []byte) {
	switch request := message.Type.(type) {
	case *media_manager.Request_Fileslist:
		handleListFiles(request, output)
	case *media_manager.Request_Unrar:
		log.Print("Received unrar request")
	default:
		log.Printf("Unexpected message type %T", request)
	}
}

func handleListFiles(request *media_manager.Request_Fileslist, output chan []byte) {
	files, err := ListFiles(request.Fileslist.Location)

	response := &media_manager.Response{
		Type: &media_manager.Response_Fileslist{
			Fileslist: &media_manager.FilesListResponse{
				Location:  request.Fileslist.Location,
				Filenames: files,
			},
		},
	}

	data, err := proto.Marshal(response)
	if err != nil && err.Error() != "EOF" {
		log.Printf("ERROR: %+v", err)
	}

	select {
	case output <- data:
	case <-time.After(time.Second * 10):
		log.Printf("ERROR: failed to write output")
	}
}

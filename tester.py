import socket
import struct

import sys

from remote.protos.message_pb2 import Request, Response

METADATA_PACKER = struct.Struct('!H')

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 4896)
    s.connect(server_address)

    message = Request()
    message.fileslist.location = 1

    message_bytes = message.SerializeToString()
    metadata_bytes = METADATA_PACKER.pack(len(message_bytes))

    s.sendall(metadata_bytes)
    s.sendall(message_bytes)

    with s.makefile('rb') as response:
        metadata_bytes = response.read(METADATA_PACKER.size)
        size, = METADATA_PACKER.unpack(metadata_bytes)

        data_bytes = response.read(size)
        data = Response()
        data.ParseFromString(data_bytes)

        print(data.fileslist.filenames)

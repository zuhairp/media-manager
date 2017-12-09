import sys
sys.path.append('..')

from gevent import monkey
monkey.patch_all()

import time
import struct

from typing import Any, Tuple
from socket import socket

import gevent

from gevent.server import StreamServer
from gevent.queue import Channel

from protos.message_pb2 import Request as RequestMessage, Response as ResponseMessage

from utils import try_read_channel, try_write_channel
import handlers

METADATA_UNPACKER = struct.Struct('!H')

def writer(client: socket, output: Channel, cancel: Channel):
    '''This greenlet is spawned to send output back to the client'''
    with client.makefile('wb') as client_output:
        cancelled = False
        while not cancelled:
            has_data, data = try_read_channel(output, timeout=1)
            if (has_data):
                metadata = METADATA_UNPACKER.pack(len(data))

                client_output.write(metadata)
                client_output.write(data)
                client_output.flush()

            cancelled, _ = try_read_channel(cancel, timeout=0)
    
def reader(client: socket, output: Channel, cancel: Channel):
    '''This greenlet is spawned to monitor the client for incoming requests'''
    with client.makefile('rb') as client_input:
        while 1:
            metadata_bytes = client_input.read(METADATA_UNPACKER.size)

            if (len(metadata_bytes) < METADATA_UNPACKER.size):
                # Probably received EOF, so shut everything down
                try_write_channel(cancel, True, timeout=-1)
                return

            message_size, = METADATA_UNPACKER.unpack(metadata_bytes)

            message_bytes = client_input.read(message_size)

            if (len(message_bytes) < message_size):
                # Probably received EOF, so shut everything down
                try_write_channel(cancel, True, timeout=-1)
                return

            message = RequestMessage()
            message.ParseFromString(message_bytes)

            message_type = message.WhichOneof('type')
            message_handler = handlers.HANDLERS[message_type]
            message_handler(message, output, cancel)
            

def connection_handler(client_socket: socket, address: Tuple[str, int]):
    '''This greenlet is spawned for each client that connects to the server'''

    print('New connection from %s:%s' % address)

    try:
        output = Channel()
        cancel = Channel()
        r = gevent.spawn(reader, client_socket, output, cancel)
        w = gevent.spawn(writer, client_socket, output, cancel)
        gevent.joinall([r, w])
    finally:
        print('Disconnected %s:%s' % address)

    
if __name__ == "__main__":
    server = StreamServer(('0.0.0.0', 3296), connection_handler)
    print('Starting server on port 3296')
    server.serve_forever()

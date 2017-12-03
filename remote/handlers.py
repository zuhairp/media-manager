from typing import Any, Tuple

from time import sleep

from gevent.queue import Channel

from common.messages.message_pb2 import Request as RequestMessage, Response as ResponseMessage

from utils import try_read_channel, try_write_channel

def unrar_handler(request: RequestMessage, output: Channel, cancel: Channel):
    for i in range(1, 101):
        response = ResponseMessage()
        response.unrar.id = request.unrar.id
        response.unrar.status.completed = i
        response.unrar.status.total = 100

        try_write_channel(output, response.SerializeToString(), timeout=10)

        sleep(1)

        cancelled, _ = try_read_channel(cancel, timeout=0)
        if cancelled:
            return

HANDLERS = {
    'unrar': unrar_handler,
    'fileslist': unrar_handler
}



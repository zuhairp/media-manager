from typing import Any, Tuple

from time import sleep

from gevent.queue import Channel

from protos.message_pb2 import Request as RequestMessage, Response as ResponseMessage

import utils
from utils import try_read_channel, try_write_channel

def unrar_handler(request: RequestMessage, output: Channel, cancel: Channel):
    def on_progress(completed: int, total: int):
        response = ResponseMessage()
        response.unrar.id = request.unrar.id
        response.unrar.status.completed = completed
        response.unrar.status.total = total
        
        try_write_channel(output, response.SerializeToString(), timeout=0)
    


HANDLERS = {
    'unrar': unrar_handler,
    'fileslist': unrar_handler
}



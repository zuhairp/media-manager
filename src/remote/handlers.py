import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from typing import Any, Tuple

import os
from time import sleep

from gevent.queue import Channel

from pyprotos.message_pb2 import Request as RequestMessage, Response as ResponseMessage
from pyprotos.enums_pb2 import UNKNOWN as LOCATION_UNKNOWN, DOWNLOADS, STAGING

from . import utils, config

from .utils import try_read_channel, try_write_channel

DIRECTORIES = {
    DOWNLOADS: config.DOWNLOADS_DIRECTORY,
    STAGING: config.STAGING_DIRECTORY
}

def unrar_handler(request: RequestMessage, output: Channel, cancel: Channel):
    def on_progress(completed: int, total: int):
        response = ResponseMessage()
        response.unrar.id = request.unrar.id
        response.unrar.status.completed = completed
        response.unrar.status.total = total
        
        try_write_channel(output, response.SerializeToString(), timeout=0)


def fileslist_handler(request: RequestMessage, output: Channel, cancel: Channel):
    assert(request.fileslist.location != LOCATION_UNKNOWN)

    directory = DIRECTORIES[request.fileslist.location]

    response = ResponseMessage()
    response.fileslist.location = request.fileslist.location 

    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith('.mkv') or f.endswith('.rar'):
                logger.debug(f)
                response.fileslist.filenames.append(os.path.join(root, f))
    
    written = try_write_channel(output, response.SerializeToString(), timeout=30)
    if not written:
        logger.warn('Failed to send fileslist message')

HANDLERS = {
    'unrar': unrar_handler,
    'fileslist': fileslist_handler
}



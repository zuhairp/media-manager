import sys
import hashlib

from typing import Any, Tuple

from gevent.queue import (
    Channel, 
    Full as QueueFullException,
    Empty as QueueEmptyException)

import rarfile

def _copy_chunks_with_progress(src, dst, progress_callback=None):
    copied = 0
    data = 1

    while data:
        data = src.read(chunk_size)
        dst.write(data)
        copied += len(data)
        if progress_callback:
            progress_callback(copied, size)


def unrar_first(
    archive_filename, 
    destination_filename,
    progress_callback=None):
    chunk_size = 4096
    with rarfile.RarFile(archive_filename) as archive:
        first  = archive.infolist()[0]
        size = first.file_size
        with archive.open(first.filename) as compressed_file, open(destination_filename, 'wb') as output:
            _copy_chunks_with_progress(compressed_file, output, progress_callback)

def copy_file(src_filename, dst_filename, progress_callback=None):
    with open(src_filename, 'rb') as src, open(dst_filename, 'wb') as dst:
        _copy_chunks_with_progress(src, dst, progress_callback)

def try_read_channel(channel: Channel, timeout: int) -> Tuple[bool, Any]:
    try:
        if (timeout == 0):
            item = channel.get(block=False)
        elif (timeout > 0):
            item = channel.get(block=True, timeout=timeout)
        else:
            item = channel.get(block=True)

        return (True, item)
    except QueueEmptyException:
        return (False, None)

def try_write_channel(channel: Channel, item: Any, timeout: int) -> bool:
    try:
        if (timeout == 0):
            item = channel.put(item, block=False)
        elif (timeout > 0):
            item = channel.put(item, block=True, timeout=timeout)
        else:
            item = channel.put(item, block=True)

        return True
    except QueueFullException:
        return False
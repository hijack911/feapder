# -*- coding: utf-8 -*-
"""
Created on 2021/6/18 10:36 上午
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""
import json
import sys

from feapder.utils.log import log
from loguru import logger

log.debug(1)
log.info(1)
log.warning(1)


def sink_serializer(message):
    record = message.record
    simplified = {
        "level": record["level"].name,
        "message": record["message"],
        "timestamp": record["time"].isoformat(),
        'thread': record['thread'].name,
        'name': record['name'],
        'filename': record['file'].name,
        'function': record['function'],
        'line': record['line']
    }
    # "%(threadName)s|%(asctime)s           |%(filename)s|%(funcName)s|line:%(lineno)d|%(levelname)s| %(message)s"
    # Thread-6      |2023-05-17 13:48:05,305|request.py  |get_response|line:351|DEBUG| xxxx
    serialized = json.dumps(simplified)
    print(serialized, file=sys.stderr)


def test():
    logger.add(sink_serializer, level="INFO", format='{level}: {time} {thread} [{name}] {message}')
    logger.info("123")
    logger.debug("123")
    logger.warning("123")


# if __name__ == '__main__':
#     test()

# -*-coding:utf-8-*-

# https://docs.python.org/zh-cn/3/howto/logging.html

import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("mian")
logger.debug("这是bug日志")
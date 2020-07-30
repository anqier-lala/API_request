# -*- coding: utf-8 -*-
# @Time : 2020/7/30 19:58
# @Author : lifangfang

import  os
import  time
from  nb_log import  LogManager
from common.config_utils import config


# l_path = os.path.join( os.path.dirname(__file__),'./pythonlogs/API.log')
# print(l_path)


# logger= LogManager('newnew').get_logger_and_add_handlers(log_filename='ApiTest.log')
logger = LogManager('newdream').get_logger_and_add_handlers(log_path=config.LOG_PATH,log_filename='ApiTest_%s.log'%time.strftime('%Y_%m_%d'))

logger.info("hello")
logger.error("this is error")
print('hello1')
logger.warning("this is warning")
print('hello2')

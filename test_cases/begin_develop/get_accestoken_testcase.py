# -*- coding: utf-8 -*-
# @Time : 2020/6/7 23:45
# @Author : lifangfang

import unittest
from common import common_api
from common.log_utils import logger


class get_access_token_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        logger.info('[case01] 正常获取access_token值测试')
        res_obj= common_api.get_access_token('client_credential', 'wxc036fc4ba09c7c16', 'bc85b7bc56a9c6bb2d7011f758ab9d7e')
        self.assertEqual(res_obj.json()['expires_in'],7200)

    def test_appid_error(self):
        self._testMethodDoc = '[case02] appid错误时，返回40013' #  会显示在报告的说明中
        logger.info('[case02] appid错误时测试')    #打印日志
        res_obj= common_api.get_access_token('client_credential', 'wxc036fc4b', 'bc85b7bc56a9c6bb2d7011f758ab9d7e')
        self.assertEqual(res_obj.json()['errcode'],40013)


if __name__ == '__main__':
    unittest.main()

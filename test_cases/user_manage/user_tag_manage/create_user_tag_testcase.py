# -*- coding: utf-8 -*-
# @Time : 2020/6/7 22:53
# @Author : lifangfang

import unittest
from common.log_utils import logger
from common.common_api import create_user_tag


class create_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_create_user_tag(self):
        logger.info('[case03] 创建用户标签接口')
        self.assertEqual(create_user_tag('LFF002').json()['tag']['name'],'LFF002')

    def test_create_user_tag_toolong(self):
        logger.info('[case04] 创建用户标签接口，标签名不能超过30字节')
        self.assertEqual(create_user_tag('不能超过30个字节我来试试abcdefg').json()['errcode'],45158)



if __name__ == '__main__':
    unittest.main()






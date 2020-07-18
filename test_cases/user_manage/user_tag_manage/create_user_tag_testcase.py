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
        self._testMethodDoc = '[case03] 验证创建标签是否可正常创建' #  会显示在报告的说明中
        logger.info('[case03] 验证创建标签是否可正常创建')
        self.assertEqual(create_user_tag('P071802').json()['tag']['name'],'P071802')

    def test_create_user_tag_toolong(self):
        self._testMethodDoc = '[case04] 验证创建标签名长度超过30个字节返回45158' #  会显示在报告的说明中
        logger.info('[case04] 验证创建标签名长度超过30个字节返回45158')
        self.assertEqual(create_user_tag('不能超过30个字节我来试试abcdefg').json()['errcode'],45158)



if __name__ == '__main__':
    unittest.main()






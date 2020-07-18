# -*- coding: utf-8 -*-
# @Time : 2020/6/18 12:53
# @Author : lifangfang

import unittest
from common.log_utils import logger
from common.common_api import modify_tags


class modify_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_modify_user_tag(self):
        self._testMethodDoc = '[case06] 验证修改标签是否可正常修改' #  会显示在报告的说明中
        logger.info('[case06] 验证修改标签是否可正常修改')
        self.assertEqual(modify_tags(106,"modify_name3").json()['errcode'],0)


    def test_modify_user_tag_toolong(self):
        self._testMethodDoc = '[case07] 验证修改标签标签名超过30个字节修改异常'
        logger.info('[case07] 验证修改标签标签名超过30个字节修改异常')
        self.assertEqual(modify_tags(103,'不能超过30个字节我来试试abcdefg43333232').json()['errcode'],45158)


if __name__ == '__main__':
    unittest.main()






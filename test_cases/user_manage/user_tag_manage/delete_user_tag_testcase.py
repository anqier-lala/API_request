# -*- coding: utf-8 -*-
# @Time : 2020/6/18 12:53
# @Author : lifangfang

import unittest
from common.log_utils import logger
from common.common_api import delete_tags


class delte_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_delete_user_tag(self):
        self._testMethodDoc = '[case07] 验证删除标签是否可正常删除' #  会显示在报告的说明中
        logger.info('[case07] 验证删除标签是否可正常删除')
        self.assertEqual(delete_tags(105).json()['errcode'],0)


    def test_delete_system_tag_do_not(self):
        self._testMethodDoc = '[case08] 验证不能修改0/1/2这三个系统默认保留的标签'
        logger.info('[case08] 验证不能修改0/1/2这三个系统默认保留的标签')
        self.assertEqual(delete_tags(1).json()['errcode'],45058)


if __name__ == '__main__':
    unittest.main()






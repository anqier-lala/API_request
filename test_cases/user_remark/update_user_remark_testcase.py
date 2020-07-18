# -*- coding: utf-8 -*-
# @Time : 2020/6/7 22:53
# @Author : lifangfang

import unittest
from common.log_utils import logger
from common.common_api import set_usermark


class create_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_set_user_mark(self):
        self._testMethodDoc = '[case10] 验证正常设置用户备注名'
        logger.info('[case10] 验证正常设置用户备注名')
        self.assertEqual(set_usermark('ooNCF540dmwadl16Nha9FI9uUBWI','souzi').json()['errcode'],0)

    def test_set_user_mark_openid_wrong(self):
        self._testMethodDoc = '[case11] 设置用户备注openid错误时候提示无效' #  会显示在报告的说明中
        logger.info('[case11] 设置用户备注openid错误时候提示无效')
        self.assertEqual(set_usermark('ooNCF540dmwadl16Nha9FI9uUBWI2121','souzi').json()['errcode'],40003)


if __name__ == '__main__':
    unittest.main()






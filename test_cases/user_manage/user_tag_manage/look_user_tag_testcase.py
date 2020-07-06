# -*- coding: utf-8 -*-
# @Time : 2020/6/8 23:22
# @Author : lifangfang


import unittest
from common.log_utils import logger
from common.common_api import look_user_tags


class look_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_look_user_tag(self):
        logger.info('[case05] 查看已创建的用户的标签接口')
        self.assertEqual(look_user_tags().json()['tags'][0]['name'],'星标组')

if __name__ == '__main__':
    unittest.main()
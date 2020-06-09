# -*- coding: utf-8 -*-
# @Time : 2020/6/7 22:53
# @Author : lifangfang

import requests
import unittest
import json
from utils import common_api
from utils.common_api import create_user_tag
from utils.config_utils import config

class create_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_create_user_tag(self):
        self.assertEqual(create_user_tag('3333yingwen').json()['tag']['name'],'3333yingwen')

    def test_create_user_tag_toolong(self):
        self.assertEqual(create_user_tag('不能超过30个字节我来试试abcdefg').json()['errcode'],45158)



if __name__ == '__main__':
    unittest.main()






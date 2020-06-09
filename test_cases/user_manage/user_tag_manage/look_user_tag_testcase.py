# -*- coding: utf-8 -*-
# @Time : 2020/6/8 23:22
# @Author : lifangfang


import requests
import unittest
import json
from utils import common_api
from utils.common_api import look_user_tags
from utils.config_utils import config


class look_user_tag_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_look_user_tag(self):
        self.assertEqual(look_user_tags().json()['tags'][0]['name'],'星标组')

if __name__ == '__main__':
    unittest.main()
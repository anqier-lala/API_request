# -*- coding: utf-8 -*-
# @Time : 2020/6/7 23:45
# @Author : lifangfang

import requests
import unittest
import json
from utils import common_api
from utils.config_utils import config


class get_access_token_api(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        res_obj=common_api.get_access_token('client_credential','wxc036fc4ba09c7c16','bc85b7bc56a9c6bb2d7011f758ab9d7e')
        self.assertEqual(res_obj.json()['expires_in'],7200)

    def test_appid_error(self):
        res_obj=common_api.get_access_token('client_credential','wxc036fc4b','bc85b7bc56a9c6bb2d7011f758ab9d7e')
        self.assertEqual(res_obj.json()['errcode'],40013)


if __name__ == '__main__':
    unittest.main()

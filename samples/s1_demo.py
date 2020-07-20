# -*- coding: utf-8 -*-
# @Time : 2020/7/19 9:03
# @Author : lifangfang

import ast
import re
import requests
import jsonpath
from common.config_utils import config
from common.check_utils import CheckUtils
from common.requests_utils import RequestsUtils
from requests.exceptions import RequestException


# res = requests.get(url='https://chrome.google.com.hk/')
# print(res.status_code)

# ##处理异常
# try:
#     number_list=[1,2,3,4,5]
#     print(number_list[6])
# except IndexError as e:
#     print('索引错误')
# except Exception as  e:   #已知可能会发生的异常，写前面，不确定的异常拿出来，写在最后
#     print('系统错误')
#
# print('hello')

# test_data=[{'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01',
#  '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)':
#  '{"grant_type":"client_credential","appid":"wxc036fc4ba09c7c16","secret":"bc85b7bc56a9c6bb2d7011f758ab9d7e"}',
#  '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in'}]

# RequestsUtils().request_by_step(test_data)

##新增标签
test_data1=[{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)':
 '{"grant_type":"client_credential","appid":"wxc036fc4ba09c7c16","secret":"bc85b7bc56a9c6bb2d7011f758ab9d7e"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token',
  '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
   {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}',
'提交数据（post）': '{"tag" : {"name" : "P1P2004"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"P1P2004"}}'}]

RequestsUtils().request_by_step(test_data1)



#!/usr/bin/env python
# encoding: utf-8
# @author: lifangfang
# @file: requests_demo.py
# @time: 2020/7/6 09:57 下午

import requests

hosts = 'https://api.weixin.qq.com'
# 获取token
params = {
    'grant_type':'client_credential',
    'appid':'wxc036fc4ba09c7c16',
    'secret':'bc85b7bc56a9c6bb2d7011f758ab9d7e'
}
res01 = requests.get( url = hosts+'/cgi-bin/token',
                      params = params
                      )
token_id = res01.json()['access_token']

# 创建一个标签
get_params = {
    'access_token': token_id
}
post_params = '{ "tag" : { "name" : "YGJ001" } }'
headers = {
    'content_type':'application/json'
}
res02 = requests.post( url = hosts+'/cgi-bin/tags/create',
                       params = get_params,
                       data = post_params,
                       headers = headers
                       )
print( res02.json() )



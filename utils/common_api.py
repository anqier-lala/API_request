# -*- coding: utf-8 -*-
# @Time : 2020/6/7 22:35
# @Author : lifangfang

import requests
from utils.config_utils import config
import re
import json

def get_access_token(grant_type,appid,secret):
    url=config.hosts + '/cgi-bin/token'
    get_param_data={
        'grant_type':grant_type,
        'appid':appid,
        'secret':secret
        }
    respose_obj=requests.get(url=url,
                             params=get_param_data)
    return respose_obj

def get_default_access_token():
    respose_obj = get_access_token('client_credential', 'wxc036fc4ba09c7c16','bc85b7bc56a9c6bb2d7011f758ab9d7e')
    return respose_obj

def create_user_tag(tag_name):
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    # 创建标签
    url = config.hosts +'/cgi-bin/tags/create'
    data = {'access_token': token_value}  # token值为之前获取access_token的值
    info = {'tag': {'name': tag_name}}
    headers = {'Content-Type': 'application/json'}  # 发送json数据必带的头部信息
    respose_obj = requests.post(url,
                                params=data,
                                data=json.dumps(info),
                                headers=headers)
    return respose_obj

def look_user_tags():
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    url = config.hosts +'/cgi-bin/tags/get'
    get_param_data = {'access_token': token_value}
    respose_obj = requests.get(url=url,
                               params=get_param_data)
    return respose_obj

if __name__ == '__main__':
    print(get_default_access_token().content)
    # print(create_user_tag('喜欢9').content)
    print(look_user_tags().content)






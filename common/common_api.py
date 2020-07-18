# -*- coding: utf-8 -*-
# @Time : 2020/6/7 22:35
# @Author : lifangfang

import requests
from common.config_utils import config
import re
import json

#获取token
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

#默认获取token
def get_default_access_token():
    respose_obj = get_access_token('client_credential', 'wxc036fc4ba09c7c16','bc85b7bc56a9c6bb2d7011f758ab9d7e')
    return respose_obj

# 创建标签
def create_user_tag(tag_name):
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    url = config.hosts +'/cgi-bin/tags/create'
    data = {'access_token': token_value}  # token值为之前获取access_token的值
    info = {'tag': {'name': tag_name}}
    headers = {'Content-Type': 'application/json'}  # 发送json数据必带的头部信息
    respose_obj = requests.post(url=url,
                                params=data,
                                data=json.dumps(info),
                                headers=headers)
    return respose_obj

 #查看标签
def look_user_tags():
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    url = config.hosts +'/cgi-bin/tags/get'
    get_param_data = {'access_token': token_value}
    respose_obj = requests.get(url=url,
                               params=get_param_data)
    return respose_obj

# 编辑标签
def modify_tags(id,name):
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    url = config.hosts +'/cgi-bin/tags/update'
    data = {'access_token': token_value}  # token值为之前获取access_token的值
    info = {   "tag" : {     "id" : id,     "name" : name  } }
    headers = {'Content-Type': 'application/json'}  # 发送json数据必带的头部信息
    respose_obj = requests.post(url=url,
                                params=data,
                                data=json.dumps(info),
                                headers=headers)
    return respose_obj

#删除标签
def delete_tags(id):
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    url = config.hosts + '/cgi-bin/tags/delete'
    data = {'access_token': token_value}  # token值为之前获取access_token的值
    info = {   "tag":{        "id" : id   } }
    headers = {'Content-Type': 'application/json'}  # 发送json数据必带的头部信息
    respose_obj = requests.post(url=url,
                                params=data,
                                data=json.dumps(info),
                                headers=headers)
    return respose_obj

#设置用户名备注
def set_usermark(openid,remark):
    token_value = re.findall('"access_token":"(.+?)"', get_default_access_token().content.decode('utf-8'))
    url = config.hosts + '/cgi-bin/user/info/updateremark'
    data = {'access_token': token_value}  # token值为之前获取access_token的值
    info = {"openid":openid, "remark":remark }
    headers = {'Content-Type': 'application/json'}  # 发送json数据必带的头部信息
    respose_obj = requests.post(url=url,
                                params=data,
                                data=json.dumps(info),
                                headers=headers)
    return respose_obj

if __name__ == '__main__':
    # print(get_default_access_token().content.decode('utf-8'))
    # print(create_user_tag('P180121212121212121212121212不能超过10个1').content.decode('utf-8'))
    print(look_user_tags().content.decode('utf-8'))
    # print(modify_tags(102,"modify_name1").content.decode('utf-8'))
    print(delete_tags(141).content.decode('utf-8'))
    print(set_usermark('ooNCF540dmwadl16Nha9FI9uUBWI','souzi1').content.decode('utf-8'))
    print(look_user_tags().content.decode('utf-8'))










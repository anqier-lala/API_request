# -*- coding: utf-8 -*-
# @Time : 2020/7/07 10:40 下午
# @Author : lifangfang

from collections import OrderedDict
import requests
import re

session_req = requests.session()
response01=session_req.get(url='http://47.107.178.45/phpwind/')   #进入首页
body=response01.content.decode('utf-8')
token_id=re.findall('name="csrf_token" value="(.+?)"/>',body)[0]


get_params={
    "m":"u",
    "c":"register",
    "a":"welcome"
            }

headerinfos={
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36    "
            }


response02=session_req.get(url="http://47.107.178.45/phpwind/index.php", #进入注册页第一步
                            params=get_params,
                            headers=headerinfos
                            )

body1=response02.content.decode('utf-8')

##注册
get_params01={
    "m": "u",
    "c": "register",
    "a":"dorun"
}

headerinfos_01={
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded"
            }

postdata={
     "username":"lifangfang06",
     "password":"123456",
     "repassword":"123456",
     "email":"2749397620@qq.com",
     "csrf_token":token_id
        }

response03 = session_req.post( url='http://47.107.178.45/phpwind/index.php', #登录
                              params = get_params01,
                              headers = headerinfos,
                              data= postdata
                              )

body2=response03.content.decode('utf-8')
print(body2)



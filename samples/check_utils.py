#!/usr/bin/env python
# encoding: utf-8
# @author: lifangfang
# @file: check_utils.py
# @time: 2020/7/18 10:30 上午

import re
import ast

class CheckUtils():
    def __init__(self,check_response=None):
        self.ck_response=check_response
        self.ck_rules = {
            '无': self.no_check,
            'json键是否存在': self.check_key,
            'json键值对': self.check_keyvalue,
            '正则匹配': self.check_regexp
        }
        self.pass_result = {
            'code': 0,
            'response_reason': self.ck_response.reason,
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result': True,
            'message': ''  # 扩招作为日志输出等
        }
        self.fail_result = {
            'code': 2,
            'response_reason': self.ck_response.reason,
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result': False,
            'message': ''  # 扩招作为日志输出等
        }


    def no_check(self):
        return self.pass_result


    def check_key(self,check_data=None):
        check_data_list = check_data.split(',')   #把需要判断的值做切割，取出键值
        res_list = [] #存放每次比较的结果
        wrong_key = [] #存放比较失败key
        for check_data in check_data_list:   #把切割的键值和取出响应结果中的所有的键一个一个对比
            if check_data in self.ck_response.keys():
                res_list.append(self.pass_result )
            else:
                res_list.append( self.fail_result )
                wrong_key.append(check_data)     #把失败的键放进来，便于后续日志输出
        # print(res_list)
        # print(wrong_key)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self,check_data=None):
        res_list = []  # 存放每次比较的结果
        wrong_items = []  # 存放比较失败 items
        for check_item in ast.literal_eval(check_data).items():  #literal_eval()安全性的把字符串转成字典，items（）取出键值对
            if check_item in self.ck_response.items():
                res_list.append( self.pass_result )
            else:
                res_list.append( self.fail_result )
                wrong_items.append(check_item)
        # print( res_list )
        # print( wrong_items )

        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self,check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern,string=self.ck_response):  #匹配到了，不为空，为true
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self,check_type=None,check_data=None):
        code = self.ck_response.status_code
        if code == 200:
            if check_type in self.ck_rules.keys():
                result=self.ck_rules[check_type](check_data)
                return result
            else:
                self.fail_result['message'] = '不支持%s判断方法'%check_type
                return self.fail_result
        else:
            self.fail_result['message'] = '请求的响应状态码非%s'%str(code)
            return self.fail_result




if __name__=="__main__":
   # 检查键是否存在,{"access_token":"hello","expires_":7200} 设为响应结果,"access_token,expires_in" 为检查对象值
    CheckUtils({"access_token":"hello","expires_":7200}).check_key("access_token,expires_in")
    #检查键值对是否存在
    CheckUtils({"access_token":"hello","expires_i":7200}).check_keyvalue('{"expires_in": 7200}')
    #正则对比
   #TURE
    print(CheckUtils('{"access_token":"hello","expires_in":7200}').check_regexp('"expires_in":(.+?)'))
   #False
    print(CheckUtils('{"access_token":"hello","expires":7200}').check_regexp('"expires_in":(.+?)'))




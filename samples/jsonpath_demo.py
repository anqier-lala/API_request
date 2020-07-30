# -*- coding: utf-8 -*-
# @Time : 2020/7/30 18:39
# @Author : lifangfang


import  jsonpath

#使用jsonpath处理json数据
d1={"token":"hjshdsjhdsjadhsa","expire":"7200"}
print( jsonpath.jsonpath(d1,'$.token')[0])
#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo.py
# @time: 2020/7/5 10:42 上午


a = {'one': 1, 'two': 2, 'three': 3}
# a['one'] = 3.2
a.setdefault('four', 4)
a.setdefault('one', 3.2)
print(a)

lista = [
    {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01'},
    {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02'}
]

# case_list = {}
# for i in lista:
#     case_list.setdefault( "case_info",[] ).append(i)
# print( case_list )


case_dict = {}
for i in lista:
    case_dict.setdefault( i["测试用例编号"],[] ).append(i)
# print( case_dict )

case_list = []
for k,v in case_dict.items():
    case_dict = {}
    case_dict["case_name"] = k
    case_dict["case_info"] = v
    case_list.append( case_dict )

for c in case_list:
    print( c )

# 字典转列表


# all_case_list = []
# for i in lista:
    # all_case = {}
    # case_list.setdefault(i['测试用例编号'], []).append(i)  # 核心
    # all_case[ "case_name" ] = i['测试用例编号']
    # all_case[ "case_info" ] = case_list[ i['测试用例编号'] ]
    # all_case_list.append( all_case )

# print( all_case_list )

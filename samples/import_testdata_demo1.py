# -*- coding: utf-8 -*-
# @Time : 2020/7/20 22:17
# @Author : lifangfang

from common.requests_utils import RequestsUtils
from common.testdata_utils import TestdataUtils

all_case_info=TestdataUtils().def_testcase_data_list()
# case_info=all_case_info[0].get('case_info')
# RequestsUtils().request_by_step(case_info)

#实现执行Excel中的所有案例
for  case_info in  all_case_info:
    RequestsUtils().request_by_step(case_info.get('case_info'))
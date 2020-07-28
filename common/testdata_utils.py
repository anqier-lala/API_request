#!/usr/bin/env python
# encoding: utf-8
# @author: lifangfang
# @file: testdata_utils.py
# @time: 2020/7/6 11:01 下午

import os
from common.excel_utils import ExcelUtils
from common.config_utils import config
from common.sql_utils import SqlUtils

current_path = os.path.dirname(__file__)
test_data_path = os.path.join( current_path,'..', config.CASE_DATA_PATH )

class TestdataUtils():
    def __init__(self,test_data_path = test_data_path):
        self.test_data_path = test_data_path
        self.test_data_sheet = ExcelUtils(test_data_path, "Sheet1")
        self.test_data = self.test_data_sheet.get_sheet_data_by_dict()
        self.test_data_by_mysql = SqlUtils().get_mysql_test_case_info()

    def __get_testcase_data_dict(self):
        testcase_dict = {}
        for row_data in self.test_data:
            if row_data['用例执行'] == '是':
                testcase_dict.setdefault( row_data['测试用例编号'],[] ).append( row_data )
        return testcase_dict

    def def_testcase_data_list(self):
        testcase_list = []
        for k,v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict["case_info"] = v
            testcase_list.append( one_case_dict )
        return testcase_list

    #sql数据源
    def __get_testcase_data_dict_by_mysql(self):
        testcase_dict = {}
        for row_data in self.test_data_by_mysql:
            testcase_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return testcase_dict

    def def_testcase_data_list_by_mysql(self):
        testcase_list = []
        for k, v in self.__get_testcase_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict["case_id"] = k
            one_case_dict["case_info"] = v
            testcase_list.append(one_case_dict)
        return tuple(testcase_list)
    #获取行
    def get_row_num(self, case_id, case_step_name):
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break;
        return j + 1


    # 给出案例编号和测试步骤写入指定行的测试结果
    def write_result_to_excel(self, case_id, case_step_name, content="通过"):
        row_id = self.get_row_num(case_id, case_step_name)
        self.test_data_sheet.update_excel_data(row_id, 14, content)

    #清空测试结果
    def clear_result_from_excel(self):
        # 方法思路是对的，但是xlutils不支持
        # row_count = self.test_data_sheet.get_row_count()
        # # self.test_data_sheet.update_excel_data(2, 14, "")
        # for row_id in range(1,row_count):  # 1--5
        #     self.test_data_sheet.update_excel_data( row_id,14,"")
        row_count = self.test_data_sheet.get_row_count()
        self.test_data_sheet.clear_excel_column(1,row_count,14)


if __name__=="__main__":
    testdataUtils = TestdataUtils()
    for i in testdataUtils.def_testcase_data_list_by_mysql():
        print( i )

    row = testdataUtils.get_row_num('case03','step_02')
    print(row)




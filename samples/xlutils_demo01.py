#!/usr/bin/env python
# encoding: utf-8
# @author: lifangfang
# @file: xlutils_demo.py
# @time: 2020/7/25 12:58 下午

import os
import xlrd
from xlutils.copy import copy
from common.config_utils import config



excel_path = os.path.join( os.path.dirname(__file__) ,'..', config.CASE_DATA_PATH )
wb = xlrd.open_workbook( excel_path,formatting_info=True)  # 创建工作薄对象 xlrd模块2007 2003

new_workbook = copy(wb)  #   将new_workbook变成可写的对象 xlwt 对象
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))     #sheet_by_name('Sheet1')
sheet.write(2,14,'测试失败')
new_workbook.save(excel_path)


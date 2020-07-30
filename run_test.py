# -*- coding: utf-8 -*-
import os
import unittest
from common import HTMLTestReportCN
from  nb_log import  LogManager


current_path=os.path.dirname(__file__)
report_path=os.path.join(current_path,'reports/')
cases_path=os.path.join(current_path,'test_cases')

#方式一
# html_path=os.path.join( report_path,'report_%s.html'%(time.strftime('%Y_%m_%d_%H_%M_%S')))
# discover=unittest.defaultTestLoader.discover(start_dir=cases_path,
#                                              pattern='*_testcase.py',
#                                              top_level_dir=cases_path)
#
# main_suite=unittest.TestSuite()
# main_suite.addTest( discover )
# file=open(html_path,'wb')
# html_runner=HTMLTestRunner.HTMLTestRunner(stream=file,
#                                           title='微信api测试',
#                                           description='微信api测试')
# html_runner.run(main_suite)
# file.flush()
# file.close()


#方式二
class RunAllCases:
    def __init__(self):
        self.test_case_path = cases_path
        self.report_path = report_path
        self.title = '微信公众号测试报告'
        self.description = 'lifangfang_test'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir = self.test_case_path,
                                                       pattern='*_testcase.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='lifangfang')
        runner.run(all_suite)
        fp.close()
        return dir_path  #返回测试结果的路径

if __name__ == '__main__':
  RunAllCases().run()




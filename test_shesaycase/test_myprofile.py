# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests



class Testprofile():

    def setup_class(self):
        self.accessId = ReadConfig().get_accessid('accessId')
        self.url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/myprofile'
        self.accesstime = PublicUtils().location_time()

    @allure.feature('资料页接口')
    @allure.story('个人资料')
    @allure.severity('blocker')
    def test_myprofile(self):
        '''
        myprofile接口用例
        '''

        # accessId = ReadConfig().get_accessid('accessId')
        # url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/myprofile'
        # accesstime = PublicUtils().location_time()
        # url = ReadConfig.get_host('online_host')+ ReadConfig.get_path('app_path') + 'v1/myprofile'
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
	        "accessId": self.accessId,
	        "accessTime": self.accesstime,
	        "allowAppNotice": 1
            }
        data['accessSign'] = App_sign().get_sign(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(self.url, data=json.dumps(data), headers=header)
        # allure.attach(json.dumps(resq.json(),ensure_ascii=False), "响应", allure.attachment_type.JSON)
        # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)
        # except:
        #     print('接口失败')
        #     allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_myprofile.py'])
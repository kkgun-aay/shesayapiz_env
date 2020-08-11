# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Test_passrecent:

    def setup_class(self):
        self.accessId = ReadConfig().get_accessid('accessId')
        self.url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/passrecent'
        self.accesstime = PublicUtils().location_time()

    @allure.feature('今日推荐')
    @allure.story('我无感的人数据')
    @allure.severity('blocker')
    def test_passrecent(self):
        '''
        passrecent接口用例
        '''
        # accessId = ReadConfig().get_accessid('accessId')
        # url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/passrecent'
        # accesstime = PublicUtils().location_time()
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
            'accessTime': self.accesstime,
            'accessId': self.accessId
        }

        data['accessSign'] = App_sign().get_sign(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(self.url, data=json.dumps(data), headers=header)
        # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'userList' in resq.json()
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)
        # except:
        #     print(resq.json())
        #     print('接口请求失败')
        #     allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_passrecent.py'])

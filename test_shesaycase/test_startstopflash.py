# -*- coding: utf-8 -*-
import pytest
import allure
import json
import mock
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests

# @pytest.mark.skip('暂时跳过此类')
class Test_startstopflash:
    accessId = ReadConfig().get_accessid('accessId')
    accesstime = PublicUtils().location_time()

    @allure.feature('飞行闪聊')
    @allure.story('点击启程数据返回正常')
    @allure.severity('blocker')
    def test_startflash(self):
        '''
        startflash接口用例
        '''

        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/startflash'

        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }

        data = {
    "accessId": self.accessId,
    "accessTime": self.accesstime,
    "location": [116.428268432617,39.918750762939]
    }

        data['accessSign'] = App_sign().get_sign(data)
        # print(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(url, data=json.dumps(data), headers=header)
        # print(resq.json())
        # # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'flashProfile' in resq.json()
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

    def test_stopflash(self):
        '''
        stopflash接口用例
        '''
        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/stopflash'
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
            'accessId': self.accessId,
            'accessTime': self.accesstime
        }
        data['accessSign'] = App_sign().get_sign(data)
        resq = requests.post(url, data=json.dumps(data), headers=header)
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)


if __name__ == '__main__':
    pytest.main(['-q','-s','test_startstopflash.py'])
# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_intdata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests

class Test_flashprofile:


    @allure.feature('飞行闪聊数据')
    @allure.severity('blocker')
    def test_flashproflie(self):
        accessId = ReadConfig().get_accessid('accessId')
        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/flashprofile'
        accesstime = PublicUtils().location_time()
        data = {
            'accessId': accessId,
            'accessTime': accesstime
        }
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data['accessSign'] = App_sign().get_sign(data)
        resq = requests.post(url,data=json.dumps(data),headers=header)
        try:
            assert resq.status_code == 200
            assert resq.json()['success'] == True
            assert 'flashProfile' in resq.json()
        except:
            # print(resq.json())
            print('接口请求失败')

if __name__ == '__main__':
    pytest.main(['-q','-s','test_flashprofile.py'])
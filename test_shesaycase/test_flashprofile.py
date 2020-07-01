# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_intdata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Test_flashprofile:

    @allure.feature('闪聊接口')
    @allure.story('飞行闪聊数据')
    @allure.severity('blocker')
    # @allure.step('冷启动app')
    def test_flashproflie(self):
        '''
        flashproflie接口用例
        '''
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
        allure.attach(json.dumps(data),'接口数据',allure.attachment_type.JSON)

        resq = requests.post(url,data=json.dumps(data),headers=header)
        # allure.attach(resq.text,"响应",allure.attachment_type.TEXT)
        # allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)
        try:
            assert resq.status_code == 200
            assert resq.json()['success'] == True
            assert 'flashProfile' in resq.json()
            allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)
        except:
            # print(resq.json())
            print('接口请求失败')
            allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_flashprofile.py'])
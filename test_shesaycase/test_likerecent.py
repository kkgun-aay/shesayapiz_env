# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Test_likerecent:

    @allure.feature('今日推荐')
    @allure.story('我喜欢的人数据')
    @allure.severity('blocker')

    def test_likerecent(self):
        '''
        likerecent接口用例
        '''
        accessId = ReadConfig().get_accessid('accessId')
        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/likerecent'
        accesstime = PublicUtils().location_time()
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
            'accessTime': accesstime,
            'accessId': accessId
        }

        data['accessSign'] = App_sign().get_sign(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(url, data=json.dumps(data), headers=header)
        # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'viewMonth' in resq.json()
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)
        # except:
        #     print(resq.json())
        #     print('接口请求失败')
        #     allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_likerecent.py'])

# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Test_bookhobbies:

    @allure.feature('动态图书接口')
    @allure.story('动态图书接口返回正常')
    @allure.severity('blocker')
    def test_bookhobbies(self):
        '''
        bookhobbies图书类型接口用例
        '''
        accessId = ReadConfig().get_accessid('accessId')
        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/searchhobbies'
        accesstime = PublicUtils().location_time()
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
            'accessTime': accesstime,
            'accessId': accessId,
            'skip': 0,
            'sortByHot': 0,
            'type': 'book',
            'keyWords': ''
        }

        data['accessSign'] = App_sign().get_sign(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(url, data=json.dumps(data), headers=header)
        # print(resq.json())
        # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'hobbies' in resq.json()
        assert len(resq.json()['hobbies']) == 10
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_bookhobbies.py'])
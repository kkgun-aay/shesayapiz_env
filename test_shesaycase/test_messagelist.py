# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Test_selecemessagelist:

    def setup_class(self):
        self.accessId = ReadConfig().get_accessid('accessId')
        self.url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/selectmessagelist'
        self.accesstime = PublicUtils().location_time()

    @allure.feature('查询消息列表')
    @allure.story('消息列表数据返回正常')
    @allure.severity('blocker')
    def test_messagelistselect(self):
        '''
        selectmessagelist接口用例
        '''

        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': '*/*'
        }
        data = {
            'accessTime': self.accesstime,
            'accessId': self.accessId,
            'gender': 1,
            'findStatus': [1,3],
            'waiting': 1
        }

        data['accessSign'] = App_sign().get_sign(data)
        # print(type(data))
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)
        resq = requests.post(self.url, data=json.dumps(data), headers=header)
        print(resq.json())
        # # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'messageList' in resq.json()
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)


if __name__ == '__main__':
    pytest.main(['-q','-s','test_messagelist.py'])
# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Test_bookcreatepost:

    @allure.feature('发布图书动态接口')
    @allure.story('发布图书接口返回正常')
    @allure.severity('blocker')
    def test_bookcreatepost(self):
        '''
        bookcreatepost图书类型接口用例
        '''
        accessId = ReadConfig().get_accessid('accessId')
        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/createpost'
        accesstime = PublicUtils().location_time()
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
            'accessTime': accesstime,
            'accessId': accessId,
            'background': '#768699-#768699',
            'words': '分享一本我最近看过的书,希望你也喜欢~',
            'type': 'book',
            'hobbyId': '1084336'
        }

        data['accessSign'] = App_sign().get_sign(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(url, data=json.dumps(data), headers=header)
        print(resq.json())
        # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'pid' in resq.json()
        assert resq.json()['postCover'] == r"https://cover.intelcupid.com/book/cover/1084336.jpg"
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_createpostbook.py'])
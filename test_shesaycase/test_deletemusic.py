# -*- coding: utf-8 -*-
import pytest
import allure
import json
import requests
import time
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign


@pytest.fixture()
def get_musicpid():
    accessId = ReadConfig().get_accessid('accessId')
    accesstime = PublicUtils().location_time()
    url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/userposts'
    header = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    get_data = {
        'accessId': accessId,
        'uid': accessId,
        'accessTime': accesstime
    }
    get_data['accessSign'] = App_sign().get_sign(get_data)
    resq = requests.post(url,data=json.dumps(get_data),headers=header)
    # print(resq.json())
    return resq.json()



@allure.feature('发布动态接口')
class Test_delmusics():

    def setup_class(self):
        self.accessId = ReadConfig().get_accessid('accessId')
        self.url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/deletepost'
        self.accesstime = PublicUtils().location_time()
    # accessId = ReadConfig().get_accessid('accessId')
    # accesstime = PublicUtils().location_time()
    @allure.story('获取个人页动态数据正常')
    def test_musicpid(self,get_musicpid):
        assert get_musicpid['success'] == True
        assert 'postInfo' in get_musicpid

    time.sleep(1)
    @allure.story('删除音乐接口返回正常')
    @allure.severity('blocker')
    def test_delmusic(self,get_musicpid):
        # url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/deletepost'
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        music_pid = get_musicpid['posts'][0]['pid']
        del_data = {
            'accessTime': self.accesstime,
            'accessId': self.accessId,
            'pid': music_pid
        }
        del_data['accessSign'] = App_sign().get_sign(del_data)
        allure.attach(json.dumps(del_data), '接口数据', allure.attachment_type.JSON)

        resq = requests.post(self.url, data=json.dumps(del_data), headers=header)
        # print(resq.json())
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ =='__main__':
    pytest.main(['-q', '-s', 'test_deletemusic.py'])
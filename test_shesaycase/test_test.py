# -*- coding: utf-8 -*-
import pytest
import allure
import json
from shesay_conf.get_intdata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign
import requests


class Testprofile():

    # def __init__(self,id,time):
    #     self.id = ReadConfig.get_accessid('accessId')
    #     self.time = PublicUtils.location_time()
    # ReadConfig = ReadConfig()

    @allure.feature('个人资料')
    @allure.severity('blocker')
    def test_myprofile(self):


        accessId = ReadConfig().get_accessid('accessId')
        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/myprofile'
        accesstime = PublicUtils().location_time()
        # url = ReadConfig.get_host('online_host')+ ReadConfig.get_path('app_path') + 'v1/myprofile'
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
	        "accessId": accessId,
	        "accessTime": accesstime,
	        "allowAppNotice": 1
            }
        data['accessSign'] = App_sign().get_sign(data)

        resq = requests.post(url, data=json.dumps(data), headers=header)
        print(resq.json())

if __name__ == '__main__':
    pytest.main(['-q','-s','test_myprofile.py'])
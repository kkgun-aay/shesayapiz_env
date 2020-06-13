# -*- coding: utf-8 -*-
import time
import hashlib
import json
from shesay_utils.shesay_util import PublicUtils
from shesay_conf.get_intdata import ReadConfig


class App_sign:

    def __init__(self):
        self.read = ReadConfig()

    # @staticmethod
    # def location_time():
    #     return round(time.time() * 1000)
    # @staticmethod
    # def hash_body(body):
    #     md = hashlib.md5()
    #     md.update(body.encode('utf-8'))
    #     res = md.hexdigest()
    #     return res
    # @staticmethod
    def get_sign(self,dict_data):
        # dict_data['accessTime'] = Create_sign.location_time()
        # print(dict_data)
        accesssign = ''
        for key in sorted(dict_data):
            accesssign += key + ' ' + json.dumps(dict_data[key]) + '\n'

        # print(accesssign)
        # app_login_token = '943071f6-28e4-47f5-af2f-9870a61bc296'
        app_login_token = self.read.get_token('app_login')
        accesssign = PublicUtils.hash_body(accesssign + app_login_token)
        # dict_data['accessSign'] = accesssign
        # print(dict_data)
        # print(accesssign)
        return accesssign


if __name__=='__main__':

    data = {
	"targetId": "5ecba196b7c0b83a0de91b17",
	"inspectTime": 0,
	"accessId": "5ec3afd216b49816bd5f6a7f"
}
    # s = Create_sign()
    # s.get_sign(data)
    # Create_sign.get_sign(data)
    result = App_sign()
    result.get_sign(data)
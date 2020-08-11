# -*- coding: utf-8 -*-
import time
import hashlib
import json
from shesay_utils.shesay_util import PublicUtils
from shesay_conf.get_inidata import ReadConfig

class Backend_sign:
    def __init__(self):
        self.read = ReadConfig()

    def get_sign(self, sign_time):
        #加密方式
        backend_login_token = self.read.get_token('banckend_login')
        accesssign = PublicUtils.hash_body(backend_login_token + str(sign_time))
        # dict_data['accessSign'] = accesssign
        # print(dict_data)
        print(accesssign)
        return accesssign

    # @staticmethod
    # def pushSuggestPool(id_list):
    #     url = 'https://heihei.intelcupid.com/analyzelogs'
    #     header = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    #         'Cookie': 'zentaosid=fhbl6inr412s5afntqus7pjir6'
    #     }
    #
    #     for id in id_list:
    #         data = {
    #             "accessId": "5e9820846979ae3e53fdb0df",
    #             # "accessSign": "9985a1dbb6e0d3fbbdd15003ff83952d",
    #             "accessTime": Back_sign.location_time(),
    #             "query": "pushSuggestPool 5ecba196b7c0b83a0de91b17 " + str(id)
    #         }
    #         data["accessSign"] = Back_sign.get_sign(Back_sign.location_time())
    #         req = requests.post(url, data=data, headers=header)
    #         print(req.json())
    #         time.sleep(1)

if __name__=='__main__':
    # id_list = ['5de48f7e2782d777044c9867', '5ec5e0c0fcc88d73e190bd89','5ed627c7fd81bd313a73ba4c','5eba671303cd865537e66ed7','5dbf9cea2670af6687fbce84']
    # Backend_sign.pushSuggestPool(id_list)
    result = Backend_sign()
    result.get_sign(PublicUtils.location_time())
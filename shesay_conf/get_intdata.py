# -*- coding: utf-8 -*-
import os
import configparser

path = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(path, "shesayconf.ini")
# print(configPath)

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_token(self, param):
        value = self.cf.get("LOGINTOKEN", param)
        return value

    def get_host(self, param):
        value = self.cf.get("HOST", param)
        return value
    def get_url(self, param):
        value = self.cf.get("URL", param)
        return value
    def get_accessid(self, param):
        value = self.cf.get("ID", param)
        return value
    def get_path(self, param):
        value = self.cf.get("PATH", param)
        return value

if __name__=="__main__":
    test = ReadConfig()
    tk = test.get_accessid('accessId')
    print(tk)
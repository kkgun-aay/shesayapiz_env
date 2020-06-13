# -*- coding: utf-8 -*-
import time
import hashlib

class PublicUtils:
    @staticmethod
    def location_time():
        # print(1111)
        return round(time.time() * 1000)

    @staticmethod
    def hash_body(body):
        md = hashlib.md5()
        md.update(body.encode('utf-8'))
        res = md.hexdigest()
        # print(res)
        return res


if __name__=="__main__":
    PublicUtils.location_time()
    PublicUtils.hash_body('hhh')
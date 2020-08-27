# -*- coding: utf-8 -*-
import json
import mock
import requests

# data = {
# 	"accessId": "5ec3afd216b49816bd5f6a7f",
# 	"accessTime": 1593763555234,
# 	"location": [
# 	116.428236127496,
# 	39.918739797921],
# 	"accessSign": "272bd3ce087e5d72eb7d8f57e98787c6"
# }

data = {
            'accessTime': 1231313,
            'accessId': 23132131313,
            'gender': 1,
            'findStatus': [1,3,4],
            'waiting': 1
        }


print(type(data))

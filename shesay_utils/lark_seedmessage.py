# -*- coding: utf-8 -*-
import requests
import json
from shesay_conf.get_inidata import ReadConfig

class LarkSeedmessage:

    @staticmethod
    def seedmessage(str):
        get_url = ReadConfig()
        # url = 'https://open.feishu.cn/open-apis/bot/hook/e0033765c2804225a64d02f0e9483634'
        url = get_url.get_url('lark_url')
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "msgtype": "text",
            "title": "新包上传成功了,点击下方链接进行下载",
            "text": str
        }
        resq = requests.post(url, data=json.dumps(data), headers=headers)
        if resq.status_code == 200 and resq.json()['ok'] != False:
            # print(resq.json())
            print('消息发送成功')
        else:
            print('发送失败errcode{}'.format(resq.json()))

if __name__ == "__main__":
    LarkSeedmessage.seedmessage('hhh')
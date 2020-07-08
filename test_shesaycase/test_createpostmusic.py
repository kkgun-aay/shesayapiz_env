# -*- coding: utf-8 -*-
import pytest
import allure
import json
import requests
from shesay_conf.get_inidata import ReadConfig
from shesay_utils.shesay_util import PublicUtils
from shesay_utils.shesay_app_sign import App_sign

@allure.feature('发布动态接口')
class Test_musiccreatepost:

    accessId = ReadConfig().get_accessid('accessId')
    accesstime = PublicUtils().location_time()
    # @pytest.mark.run(order=1)
    @allure.story('发布音乐接口返回正常')
    @allure.severity('blocker')
    def test_musiccreatepost_a(self):
        '''
        musiccreatepost图书类型接口用例
        '''

        url = ReadConfig().get_host('online_host') + ReadConfig().get_path('app_path') + 'v1/createpost'

        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        data = {
            'accessTime': self.accesstime,
            'accessId': self.accessId,
            'background': '#869299-#869299',
            'words': '分享一首我最近听过的歌,希望你也喜欢~',
            'type': 'music',
            'hobbyId': '1403215687'
        }

        data['accessSign'] = App_sign().get_sign(data)
        allure.attach(json.dumps(data), '接口数据', allure.attachment_type.JSON)
        resq = requests.post(url, data=json.dumps(data), headers=header)
        # try:
        assert resq.status_code == 200
        assert resq.json()['success'] == True
        assert 'pid' in resq.json()
        assert resq.json()['postCover'] == r"https://cover.intelcupid.com/music/cover/1403215687.jpg"
        allure.attach(json.dumps(resq.json(), ensure_ascii=False), "响应", allure.attachment_type.JSON)

if __name__ == '__main__':
    pytest.main(['-q','-s','test_createpostmusic.py'])
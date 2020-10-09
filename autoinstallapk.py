# -*- coding: utf-8 -*-
from appium import webdriver
import os, time


class testinstallapk:

    def __init__(self, packgepath, screenshotpath):
        self.packgepath = packgepath
        self.screenshot = screenshotpath

    def getapklist(self):

        filelist = []
        for root, dirs, files in os.walk(self.packgepath):
            for file in files:
                if file.endswith('.apk'):
                    filelist.append(file)

            return filelist

    def testinstall(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'feee6ee6',
            'platformVersion': '9',
            "noReset": True,
            'automationName': "UiAutomator2",
            # apk包名
            'appPackage': 'com.intelcupid.shesay',
            # apk的launcherActivity
            'appActivity': 'com.intelcupid.shesay.main.PosterActivity'

        }
        for apk in self.getapklist():
            try:
                desired_caps['app'] = self.packgepath + '\\' + apk
                # print(desired_caps)

                driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

                driver.start_activity('com.intelcupid.shesay', 'com.intelcupid.shesay.main.PosterActivity')
                time.sleep(1)
                # 截图保存
                driver.get_screenshot_as_file(self.screenshot + '\\' + apk + '登录页.png')
                time.sleep(6)
                driver.remove_app("com.intelcupid.shesay")
            except Exception as e:
                print('---报错-----')
                print("{}安装包出错,具体错误信息:{}".format(apk, e))
                driver.remove_app("com.intelcupid.shesay")
                continue
            else:
                print("{}包测试完毕！".format(apk))


if __name__ == "__main__":
    testinstallapk("H:\\bug\\2020-08-25-16-58-09", 'C:\\Users\\asus\\Desktop\\install_screen').testinstall()

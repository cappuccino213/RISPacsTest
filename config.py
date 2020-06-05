#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:06
# @Author  : Zhangyp
# @File    : config.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
# 获取token
def get_token():
	import requests
	header = {'Content-Type': 'application/json'}
	url = "http://192.168.1.18:8703/Token/Retrive"  # token服务器地址
	payload = {
		"requestIP": "192.168.1.56",  # 请求客户端
		"audience": "eWordRIS",
		"customData": {},
		"expire": 240}
	res = requests.post(url, headers=header, json=payload)
	return res.json()['token']


"""测试环境配置"""
HOST = "http://192.168.1.18:8141"

"""API配置"""
API_NAME = "/api/Order/Create"
USERINFO = '{"userID": "e8153411-9c93-4eca-84c6-ab7a00a659cb", "organizationID": "0f4a7f80-b8ed-4d25-af02-ab7a009a7966", "observationDeptID": "f0ea6faf-dd09-43b6-bdd0-ab7a009b8633", "clientAuthCode": "", "useScenario": "1", "cookieRequest": {"printTaskSolution": "00000000-0000-0000-0000-000000000001", "printerSolution": "00000000-0000-0000-0000-000000000002", "equipSolution": ""}}'

HEAD = {
	'content-type': 'application/octet-stream',
	'Authorization': get_token(),
	'userInfo': '{"userID":"6588DC3C-A9C9-42CF-958D-AB8800E1C239","organizationID":"9B1E70B7-6FF1-4CEB-86F0-AB8800AE08EC","observationDeptID":"A9FBDB64-CAA1-4E71-85CC-AB8800AEF2B2","clientAuthCode":"","useScenario":"1","cookieRequest":{"printTaskSolution":"00000000-0000-0000-0000-000000000001","printerSolution":"00000000-0000-0000-0000-000000000002","equipSolution":""}}'
	# 'userInfo': USERINFO
}

"""dicom参数配置"""
#本地scu节点配置
LocalAE = 'zypModality'
Path = r'E:\my project\RISPacsTest\Images'

#节点scp配置
# AETitle = 'DYSERVICE'
AETitle = 'test001'
Addr = '192.168.1.18'
# PORT = 8191
PORT = 8192


"""任务执行参数"""
# 每次任务发送间隔，单位秒
SendInterval = 2

# 任务休息时间，单位秒
SleepTime = 2


# if __name__ == '__main__':
# 	print(get_token())

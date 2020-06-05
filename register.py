#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 13:51
# @Author  : Zhangyp
# @File    : register.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from config import HOST, API_NAME, HEAD
import requests
from FakerData import Person, choice
import json
p = Person()


def register():
	url = HOST + API_NAME
	from ProtobufPy.OrderRequestPb_pb2 import OrderRequestPb
	"""赋值第一层参数值"""
	body = OrderRequestPb()
	body.observationDeptID = 'A9FBDB64-CAA1-4E71-85CC-AB8800AEF2B2'
	body.organizationID = '9B1E70B7-6FF1-4CEB-86F0-AB8800AE08EC'
	body.serviceSectID = 'CT'
	body.name = p.name
	body.nameSpell = p.name_spell
	body.sex = p.sex
	body.birthDate = p.birth_date.strftime('%Y-%m-%d')
	body.patientClass = choice([1000, 2000, 3000, 4000])
	body.age = p.age
	body.ageUnit = '岁'
	body.chargeFlag = 1
	body.charges = 60
	body.observationLocationID = choice(
		["EFA16246-7EAE-4814-B1C1-AB8800E8EC11", "893AB276-29A0-4BCB-BE02-AB9000B74B5B"])
	body.observationLocation = 'CT'
	body.examBodyPart = "肺部常规"
	body.examBodyPartID = "43F5BC3F-AB08-43AC-B4D5-AB8800AF199A"
	body.procedureID = "CEFAE729-A430-4D22-8006-AB8800AF1D06"
	body.procedureName = "双斜位"
	body.procedureWorkload = '2.00'
	body.diagnosticGroupID = "0D029481-E380-4A3C-9B03-AB8800AF1966"
	body.allProcedureName = "双斜位"
	"""追加第二层参数值"""
	from ProtobufPy.OrderListRequestPb_pb2 import OrderListRequestPb
	olr_body = OrderListRequestPb()
	olr_body.datas.append(body)
	olr_body = olr_body.SerializeToString()
	res = requests.request(method='POST', url=url, data=olr_body, headers=HEAD)
	from ProtobufPy.PageResponsePb_pb2 import PageResponsePb
	pr_data = PageResponsePb()
	pr_data.ParseFromString(res.content)
	from ProtobufPy.OrderFinishResponsePb_pb2 import OrderFinishResponsePb
	from google.protobuf.json_format import MessageToJson
	res_json = MessageToJson(pr_data).encode('utf-8').decode("unicode_escape")
	# print(res_json.encode('utf-8').decode("unicode_escape"))
	# print(json.loads(res_json))
	return json.loads(res_json)['data'][0]['orderInfo']

# print(register()['accessionNumber'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 13:52
# @Author  : Zhangyp
# @File    : c_store_test.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from config import LocalAE, AETitle, Addr, PORT
import os
from pynetdicom import AE
from pydicom import dcmread

"""遍历影像文件"""


def find_images(path):
	images = []
	for file in os.listdir(path):
		if file.endswith('.dcm') or file.endswith('.DCM'):
			images.append(file)
	return images


"""影像c-store"""


# 日期格式处理函数
def convert_date(date_time):
	"""
	将2020/5/7 转化成20200507
	:param date_time: 带'/'的时间格式
	:return: 没有分隔符的时间
	处理方法：用/分割，根据日期的位数补零，然后拼接
	"""
	date = date_time.split(' ')[0]
	dl = date.split('/')
	if len(dl[1]) == 1:
		dl[1] = '0' + dl[1]
	if len(dl[2]) == 1:
		dl[2] = '0' + dl[2]
	date = dl[0] + dl[1] + dl[2]
	time = date_time.split(' ')[1]
	return date, time


def store_image(file, StUID, SeUID, **image):
	# 1.读取影像
	ds = dcmread(file)
	# 2.修改影像值
	ds.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2'  # 'Implicit VR Little Endian'
	ds.StudyInstanceUID = StUID
	ds.SeriesInstanceUID = SeUID
	ds.PatientID = image['patientID']
	ds.AccessionNumber = image['accessionNumber']
	ds.PatientName = image['nameSpell']
	ds.OtherPatientNames = image['name']
	# ds.StudyDate = studydate.split(' ')[0]
	ds.StudyDate = convert_date(image['observationEndDate'])[0]
	ds.StudyTime = convert_date(image['observationEndDate'])[1]
	# ds.StudyTime = studydate.split(' ')[-1]
	# ds.PerformedProcedureStepStartDate = kw['observationEndDate'].split(' ')[0]
	# ds.PerformedProcedureStepStartTime = kw['observationEndDate'].split(' ')[-1]
	# 3.Initialise the Application Entity
	# import datetime
	ae = AE(ae_title=LocalAE)
	# 4.上下文添加影像类型
	class_uid = ds['SOPClassUID'].value
	ae.add_requested_context(class_uid)
	# 5.Associate with peer AE at IP 127.0.0.1 and port 11112
	assoc = ae.associate(Addr, PORT, ae_title=AETitle)
	# 6.发送影像
	if assoc.is_established:
		# Use the C-STORE service to send the dataset #returns the response status as a pydicom Dataset
		status = assoc.send_c_store(ds)
		if status:
			# If the storage request succeeded this will be 0x0000
			print('C-STORE request status: 0x{0:04x}'.format(status.Status))
		else:
			print('Connection timed out, was aborted or received invalid response')
		# Release the association
		assoc.release()
	else:
		print('Association rejected, aborted or never connected')


if __name__ == "__main__":
	from pydicom.uid import generate_uid
	
	image_dict = {"patientID": '000002', "accessionNumber": "test2006030002", "nameSpell": "ceshi1hao", "name": "测试1号",
				  "observationEndDate": "2020/6/3 14:42:49"}
	store_image(r'E:\PyProject\RISPacsTest\Images\0900421.2.156.14702.1.1005.128.2.202005180901458573499.dic.dcm',
				generate_uid(), generate_uid(), **image_dict)

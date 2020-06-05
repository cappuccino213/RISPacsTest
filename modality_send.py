#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:07
# @Author  : Zhangyp
# @File    : modality_send.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
from c_store import find_images, store_image
from config import Path
import os
from pydicom.uid import generate_uid
from importlib import reload
# import register
# reload(register)
from register import register

"""获取登记信息"""


def get_reginfo():
	image_info = register()
	# 提取子集
	image_item = {'patientID', 'accessionNumber', 'nameSpell', 'name', 'observationEndDate'}
	image = {key: image_info[key] for key in image_info.keys() & image_item}
	print("登记成功：姓名-%s，检查号-%s，检查时间-%s" % (image['name'], image['accessionNumber'], image['observationEndDate']))
	return image


"""批量c-store"""


def send_image():
	images = find_images(Path)
	studyUID = generate_uid()
	seriesUID = generate_uid()
	reg_info = get_reginfo()
	for i in images:
		image_file = os.path.join(Path, i)
		store_image(image_file, studyUID, seriesUID, **reg_info)
	print("发送影像成功")


if __name__ == '__main__':
	send_image()

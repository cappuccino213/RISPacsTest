#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 11:13
# @Author  : Zhangyp
# @File    : dispatch.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import schedule
import time
from config import SendInterval,SleepTime


def job():
	import subprocess
	cli = "python modality_send.py"
	try:
		cl = subprocess.Popen(cli, stdout=subprocess.PIPE, shell=True)
		stdout_content = [line.decode("utf-8") for line in cl.stdout.readlines()] # 将控制台信息转化成str的list
		for i in stdout_content:
			print(i)  # 打印控制台信息
	except Exception as e:
		raise str(e)


# 任务执行策略
schedule.every(SendInterval).seconds.do(job)

# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

if __name__=='__main__':
	while True:
		schedule.run_pending()
		time.sleep(SleepTime)

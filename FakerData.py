#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 16:11
# @Author  : Zhangyp
# @File    : FakerData.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import datetime
from faker import Faker
from random import choice
from pypinyin import pinyin, Style

fake = Faker('zh_CN')  # 指定中国区域（en_US 英语（美国）、en_GB 英语（英国）等）其他提供商见https://faker.readthedocs.io/en/master/


class Person:  # 人的基本信息相关
	
	def __init__(self):
		self.name = self.name_by_sex()
		self.name_spell = self.name_spell()
		self.sex = self.sex()
		self.birth_date = self.birthday()
		self.age = self.age()
		self.address = self.address()
		self.company = self.company()
		self.job = self.job()
	
	def name_spell(self):
		pinyin_list = pinyin(self.name, style=Style.NORMAL)  # 通过pinyin函数将中文转换成list,结构[['zhong'], ['xin']]
		pinyin_str = ''
		for sub_list in pinyin_list:  # 遍历拼凑起来
			for spell in sub_list:
				pinyin_str = pinyin_str + spell.capitalize()  # 首字母大写处理
		return pinyin_str
	
	@staticmethod
	def name_by_sex(sex='F'):  # 根据性别生成姓名
		if sex == 'F':
			return fake.name_female()
		if sex == 'M':
			return fake.name_male()  # gen
	
	@staticmethod
	def birthday():  # 最大90岁的年龄
		return fake.date_of_birth(tzinfo=None, minimum_age=1, maximum_age=90)
	
	def age(self):
		return datetime.date.today().year - self.birth_date.year
	
	@staticmethod
	def sex():  # 随机生成性别
		return choice(['F', 'M'])
	
	@staticmethod
	def address():
		return fake.address()
	
	@staticmethod
	def company():
		return fake.company()
	
	@staticmethod
	def job():
		return fake.job()
	
	@staticmethod
	def phone(_type=1):  # 1表示移动电话，2表示固话
		if _type == 1:
			return fake.phone_number()
		if _type == 2:
			str1 = fake.msisdn()[0:4]
			str2 = fake.msisdn()[4:]
			return str1 + '-' + str2
	
	def generate_id(self):  # 身份证号
		pass

from datetime import datetime
import logging
import os
import allure
from DrissionPage import ChromiumPage, ChromiumOptions
from config.settings import *


class LoginPage:
	def __init__(self, page: ChromiumPage, screenshot_step=None):
		self.page = page
		self.step = screenshot_step or (lambda desc: None)
		self.page.get(f'{BASE_URL}/login')

	def click_switch_page(self):
		self.page.ele('xpath=//div[@class="toUser"]').click()
		self.step('切换到登录页面')

	def input_username(self, username: str):
		self.page.ele('xpath=//div[@class="user-name"]//input').input(username)
		self.step('输入账号')

	def input_password(self, password: str):
		self.page.ele('xpath://div[@class="pass-word"]//input').input(password)
		self.step('输入密码')

	def click_login(self):
		self.page.ele('xpath=//button[@class="odos-btn odos-btn--primary"]').click()
		self.step('点击登录')

	def select_office(self, office: str):
		self.page.ele(f'xpath=//div[@class="label"  and text()="{office}"]').click()
		self.step(f'选择诊所:{office}')

	def get_search_text(self):
		text = self.page.ele('xpath=//div[@class="search"]//input').attr('placeholder')
		self.step('进入首页')
		return text

import logging
import os

import allure
import pytest
from DrissionPage import ChromiumPage, ChromiumOptions
from config.settings import *
from datetime import datetime


@pytest.fixture(scope="function", autouse=True)
def setup_logging():
	logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')


@pytest.fixture(scope="function")
def dp():
	if not os.path.exists(SCREENSHOT_DIR):
		os.makedirs(SCREENSHOT_DIR)

	# 配置无痕浏览器，防止数据缓存
	co = ChromiumOptions()
	co.set_argument('--start-maximized')
	co.set_argument('--incognito')

	page = ChromiumPage(co)
	yield page
	page.close()


@pytest.fixture
def auto_screenshot(request, dp):
	"""
	自动截图夹具，在测试步骤中传入描述即可，自动截图并附加到 Allure。
	"""

	def take(description="步骤截图"):
		timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
		filename = f'{timestamp}_{description}.png'.replace(' ', '_').replace('|', '')
		path = os.path.join(SCREENSHOT_DIR, filename)
		os.makedirs(SCREENSHOT_DIR, exist_ok=True)
		dp.get_screenshot(path, full_page=True)
		allure.attach.file(path, name=description, attachment_type=allure.attachment_type.PNG)

	return take

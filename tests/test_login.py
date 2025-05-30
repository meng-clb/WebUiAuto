import os
import allure
from conftest import login_user


class TestLogin:
	# 登录
	@allure.feature("登录功能")
	@allure.story("正常登录流程")
	@allure.title("登录成功")
	def test_login_access(dp, auto_screenshot, login_user):
		login = login_user()
		assert '输入病历号' in login.get_search_text()

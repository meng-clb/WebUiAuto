import allure
import pytest
from pages.login_page import LoginPage


# 登录
@allure.feature("登录功能")
@allure.story("正常登录流程")
@allure.title("登录成功")
@pytest.mark.parametrize("username,password,office", [("chenlibin", "Start2025", "张江")])
def test_login_access(dp, auto_screenshot, username, password, office):
	login = LoginPage(dp, screenshot_step=auto_screenshot)
	login.click_switch_page()
	login.input_username(username)
	login.input_password(password)
	login.click_login()
	login.select_office(office)
	assert '输入病历号' in login.get_search_text()

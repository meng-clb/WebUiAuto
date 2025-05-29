# utils/screenshot.py
import os
import allure
from datetime import datetime


def attach_screenshot(page, title="截图"):
	ts = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"{ts}_{title}.png".replace(" ", "_")
	filepath = os.path.join("screenshots", filename)
	page.save_screenshot(filepath)
	allure.attach.file(filepath, name=title, attachment_type=allure.attachment_type.PNG)

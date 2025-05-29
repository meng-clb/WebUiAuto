import pytest

if __name__ == '__main__':
    pytest.main()
    """
    命令行运行
    运行测试用例
    pytest --alluredir=allure-results
    使用allure生成html文件
	allure generate allure-results -o allure-report --clean
	allure open allure-report
    """

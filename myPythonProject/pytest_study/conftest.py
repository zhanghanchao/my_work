# -*-coding:utf-8-*-
# conftest.py文件同目录必须有一个__init__.py
# conftest用户写hook函数
import pytest
import time
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(return_path(log_name))

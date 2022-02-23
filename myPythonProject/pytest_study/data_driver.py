# -*-coding:utf-8-*-
import pytest
import yaml

class TestDemo:

    @pytest.mark.parametrize('env', yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是:", env["test"])
        elif "dev" in env:
            print("这是开发环境")

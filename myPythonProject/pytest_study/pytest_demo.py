# -*-coding:utf-8-*-
import sys

import pytest


class pythondemo:

    # 用例标记-m，执行时可以选择性执行pytest xx.py -vs -m "android"
    @pytest.mark.android
    def test_android(self):
        assert 1 == 1

    @pytest.mark.android
    def test_android2(self):
        assert 1 == 1

    @pytest.mark.ios
    def test_ios(self):
        assert "ios" == "ios"

    # skip-始终跳过该case，skipif-遇到特定情况跳过case,xfail-遇到特定情况，输出预期失败的情况
    @pytest.mark.skip(reason="代码没写完")
    @pytest.mark.skipif(sys.platform == "win", reason="不是mac平台")
    @pytest.mark.xfail(reason="功能未完成")
    def test_website(self):
        pytest.skip("存在bug")
        assert "web" == "1web"

    # 参数化

    # ids重命名
    @pytest.mark.parametrize('test_input, expected', [
        ("3+6,9"), ("3+5,8"), ("35+5,40")], ids=["number1", "number2", "number3"])
    def test_mark(test_input, expected):
        assert eval(test_input) == expected
    # search_list = ['appium', 'selenium', 'pytest']
    # @pytest.mark.parametrize('name', search_list)
    # def test_search(name):
    #     assert name in search_list

    # 笛卡尔积
    @pytest.mark.parametrize("wd", ["appium", "selenium", "pytest"])
    @pytest.mark.parametrize("code", ["utf-8", "gbk", "gb2132"])
    def test_dkej(wd,code):
        print(f"wd: {wd}, code: {code}")

    # todo --lf只重新上次失败的用例，--ff：先运行失败的，再运行其他的
    # pytest --lf xxx.py
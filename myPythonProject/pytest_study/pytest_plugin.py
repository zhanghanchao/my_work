# -*-coding:utf-8-*-
# pip install pytest-ordering 控制用例的执行顺序
# pip install pytest-xdist  分布式执行用例,多线程并发执行
# pip install pytest-dependency  控制用例的依赖关系
# pip install pytest-rerunfailures  失败重跑
# pip install pytest-random-order  用例随机执行
# 搜索插件查看用法：https://pypi.org/
import pytest


# @pytest.mark.run(order=1)
# @pytest.mark.first

# 4个CPU执行，硬件有几核就用几核
# python -n 4/auto xxx.py

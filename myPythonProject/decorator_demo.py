# -*-coding:utf-8-*-
'''
闭包函数，闭包的内部函数中，对外部作用域的变量引用，闭包无法修改外部函数的局部变量，闭包可以保存当前运行环境
'''
import time


def output_stutent(grade):
    def inner(name, gender):
        print(f"hanchao的名称是{name},性别是{gender},年纪是{grade}")

    # 便于外部调用参数
    return inner


student = output_stutent(1)
student("lily", "男")
student("卡卡", "女")

# 1.定义一个外函数，外函数有一个形参，接受被装饰的函数对象
# 2.定义一个内函数，内函数内调用传入函数
# 3.定义外函数的返回值，外函数返回值固定格式为内函数对象
# 实现一个计时器的装饰器，计算函数执行时间
import datetime


def timer(func):
    # 如果被装饰函数
    def inner(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"函数的结束时间{end_time - start_time}")

    return inner


@timer
def hanchao(name, age, gender):
    print(f"hanchao's name is {name},年龄是{age},性别{gender}")
    time.sleep(2)


hanchao("arvin", 18, "男")

# -*-coding:utf-8-*-
# 类型提示功能
# 为参数和返回数据类型制定类型
# def greeting(name:str): -> str
#     return "hello" + name
from typing import List
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(1.1, [1.2, -4.2, 5.4]))

# 指定自定义类型student
class Student:
    name: str
    age: int

def get_stu(name:str) ->Student:
    return Student()

get_stu("hanchao").name

# -*-coding:utf-8-*-
import os

# 获取系统名称
# print(os.name)
# # 获取系统环境变量信息
# print(os.environ)
# # 获取指定名称得环境变量信息
# print(os.getenv('PATH'))
# 执行系统指令
# os.system('pwd')

"""os 目录相关"""
# 获取当前所在目录
# print(os.getcwd())
# 切换目录
# os.chdir('..')
# 列出当前目录下的所有文件
# print(os.listdir)
# 创建空目录
# os.mkdir('demo')
# 递归创建多级空目录
# os.makedirs('a/b/c')
# 删除空目录
# os.rmdir('demo')
# 重命名目录
# os.rename('demo', 'hello')
# 删除文件
# os.remove('a.txt')

"""os 路径相关path方法"""
# 获取绝对路径
print(os.path.abspath('os_study.py'))
# 返回文件名
print(os.path.basename("/Users/arvin/PycharmProjects/myPythonProject/os_study.py"))
# 返回文件路径
print(os.path.dirname("/Users/arvin/PycharmProjects/myPythonProject/os_study.py"))
# 分割路径
print(os.path.split("/Users/arvin/PycharmProjects/myPythonProject/os_study.py"))
# 拼接路径
print(os.path.join("/Users/arvin/PycharmProjects/myPythonProject", "os_study.py"))
# 判断路径是否存在
print(os.path.exists("/Users/arvin/PycharmProjects/myPythonProject/os_study.py"))
# 判断是否是目录
print(os.path.isdir("/Users/arvin/PycharmProjects/myPythonProject"))
# 判断是否是文件
print(os.path.isfile("/Users/arvin/PycharmProjects/myPythonProject/os_study.py"))
# 获取文件大小
print(os.path.getsize("/Users/arvin/PycharmProjects/myPythonProject/os_study.py"))
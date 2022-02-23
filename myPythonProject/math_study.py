# -*-coding:utf-8-*-
import math


# 圆周率
# print(math.pi)
# # 对数e
# # print(math.e)
# # # 正无穷大
# # print(math.inf)
# # # 非数字
# # print(math.nan)
# # 向上取整
# print(math.ceil(4.3))
# # 返回x和y的幂
# print(math.pow(3, 4))

# 每天努力一点点和每天放松一点点.基准值为1，每努力一天增加0.01。反之-0.01.
# 计算一年365天的差距。
def study_hard():
    up = math.pow((1.0 + 0.01), 365)
    down = math.pow((1.0 - 0.01), 365)
    print(f"每天努力一点点{up}\nVS\n每天贪玩一点点{down}")
#     每天努力一点点37.78343433288728
#     VS
#     每天贪玩一点点0.025517964452291125


study_hard()

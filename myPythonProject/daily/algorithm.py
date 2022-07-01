# -*-coding:utf-8-*-
def solution(s: str):
    # 字符串a乘以整数n，意思就是把a重复n次
    return ''.join(x * int(x) for x in s)

if __name__ == '__main__':
    s = "512"
    print(solution(s))
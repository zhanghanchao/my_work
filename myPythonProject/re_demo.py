# -*-coding:utf-8-*-
# 正则表达式库
import re

# 匹配包含hanchao开头的字符串
pattern = r"han\w+"
# 转换为正则对象
# prog = re.compile(pattern)
s1 = "hanchao"
match1 = re.match(pattern, s1, re.I)
m_search = re.search(pattern, s1, re.I)
print(match1)
print(m_search)
print(f"匹配值的起始位置为：{match1.start()}")
print(f"匹配值的结束位置为：{match1.end()}")
print(f"匹配值位置的元祖为：{match1.span()}")
print(f"匹配值的字符串为：{match1.string}")
print(f"匹配的数据为：{match1.group()}")

s2 = "i like hanchao"
match2 = re.match(pattern, s2, re.I)
print(match2)

# re.sub实现字符串替换
pattern2 = r"1[34578]\d{9}"
s1 = "中奖号码123456， 联系电话 156111111"
result = re.sub(pattern2, '1xxxxxxxx', s1)
print(result)
# re.split分割
p = r"[?|&]"
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A5%BD%E7%9C%8B&fenlei=256&rsv_pq=924f6a460000bf04&rsv_t=c2fbAqqlvNPhsEpnRMJ8alN98AallzSSmFwsBlRQ61ZUu%2FDFPrI1VaFjO4M&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E5%25A5%25BD%25E7%259C%258B&rsp=5&inputT=1076&rsv_sug4=1076"
r = re.split(p, url)
print(r)
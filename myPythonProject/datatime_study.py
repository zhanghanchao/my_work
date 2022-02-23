# -*-coding:utf-8-*-
import datetime

nowtime = datetime.datetime.now()
print(nowtime)
print(nowtime.day)
print(nowtime.month)
print(nowtime.year)
# 转成时间戳
print(nowtime.timestamp())
# 字符串与时间的转化
s = "2021-09-03 04:43:43"
s1 = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(s1)
# 时间转换成字符串
result = nowtime.strftime('%a,%b %d %H:%M')
print(result)
mtimestamp = 1640750691.210572
s1 = datetime.datetime.fromtimestamp(mtimestamp)
print(s1)

# 写一段代码，生成日志文件，以当前时间命名，并写入内容
c_time = nowtime.strftime("%Y%m%d_%H%M%S")
print(c_time)
log_name = c_time + '.log'
with open(log_name, 'w+', encoding='utf-8') as f:
    f.write("日志信息")
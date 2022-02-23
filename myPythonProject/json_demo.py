# -*-coding:utf-8-*-
# 主要是dumps,loads,dump,load,加s是字符串处理，没有的就是和文件有关
import json

# 定义python结构
data = {
    'a': 1,
    'b': [2, 3, 4],
    'c': '超越',
    'd': False,
    'e': None,
    'f': 5,
}
# 将python对象编码为JSON字符串,有中文得改变ensure_ascii默认值
json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)

# 定义json字符串
json_data = '''{"a": 1, "b": [2, 3, 4], "c": true, "d": false, "e": null, "f": 5}'''
# 将json字符串转化为python对象
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))

# 把python对象转化为json格式的数据并且写入json文件
with open('data.json', 'w') as f:
    json.dump(data, f)
# 读取json文件，转化为python对象
with open('data.json', 'r') as f:
    json.load(f)
    print(data)
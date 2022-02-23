# -*-coding:utf-8-*-
import json

import urllib3

def test_HTTP():
    #创建连接池对象，默认会校验证书
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"
    # 发起HTTP请求
    resp = pm.request(method='get', url=url)
    # print(type(resp))
    # print(resp.status)
    # print(resp.headers)
    # print(resp.data)
    # 获取二进制形式的响应内容
    raw = resp.data
    # 解码成字符串
    content = raw.decode('utf-8')
    print(type(content), content)
    # json解析成字典对象
    obj = json.loads(content)
    print(type(obj), obj)
def test_HEADERS():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"
    #todo 定制请求头
    headers = {'name': 'hanchao'}
    #todo 发送请求
    resp = pm.request('GET', url, headers=headers)
    #todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(type(content), content)

def test_querystr_get():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"
    #todo 定义查询字符串
    fields = {'name': 'hanchao'}
    #todo 发送请求
    resp = pm.request('GET', url, fields=fields)
    #todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(content)
def test_querystr_post():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"

    # todo 从内置库urllib的parse模块导入编码方法
    from urllib.parse import urlencode
    #todo urlencode编码
    encoded_str = urlencode({'name': 'hanchao'})
    # 拼接到url中，发送请求
    resp = pm.request('POST', url=url + '?' + encoded_str)
    #todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(content)

def test_querystr_form():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"
    #todo 定义查询字符串
    fields = {'name': 'hanchao'}
    #todo 发送请求
    resp = pm.request('POST', url, fields=fields)
    #todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(content)

# 提交json格式数据
def test_json():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"
    # 设定请求体数据
    headers = {'Content-Type': 'application/json'}
    # todo 格式化JSON文本数据
    json_str = json.dumps({'name': 'hanchao'})
    # todo 发送请求
    resp = pm.request('POST', url, headers=headers, body=json_str)
    content = json.loads(resp.data.decode('utf-8'))
    print(content)

    # 设置超时时间
def test_timeout():
    pm = urllib3.PoolManager()
    # 访问这个地址后，服务器会在3s后响应
    url = "http://httpbin.org/delay/3"

    #设置超时时间
    resp = pm.request(method="GET", url=url, timeout=4.0)
    print(resp.status)
    assert resp.status == 200

def test_HTTPS():
    url = "https://httpbin.ceshiren.com/get"
    # todo 创建不校验证书的连接池对象"CERT_NONE",需要校验："CERT_REQUIRED"
    pm_https = urllib3.PoolManager(cert_reqs="CERT_NONE")
    # todo 发送HTTPS请求
    resp = pm_https.request('GET', url)

    content = json.loads(resp.data.decode('utf-8'))
    print(type(content), content)
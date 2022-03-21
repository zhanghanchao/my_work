# -*-coding:utf-8-*-
import hashlib
import time
import uuid
import json
import xmind
import sys


# 深度递归遍历topic
def _dfs_topic(root_topic, time_stamp):
    if not root_topic:
        return
    # 组装数据
    dict_root = {
        'data': {
            'created': time_stamp,
            'text': root_topic.get('title'),
            'id': str(uuid.uuid1()),
        },
        'children': []
    }
    # 递归遍历子topic数据
    for item in root_topic.get('topics', []):
        dict_root.get('children').append(_dfs_topic(item, time_stamp))
    # 返回数据
    return dict_root


# template，theme，version，base 就给了一个默认值
def trans_xmind(xmind_json, template='right', theme='fresh-blue', version='1.4.43', base=16):
    # 创建时间戳
    time_stamp = int(round(time.time() * 1000))
    # 获取xmind中的topic根数据，请确保xmind_json中的长度大于0
    xmind_root_topic = xmind_json[0].get('topic')
    print(xmind_root_topic)
    print(xmind_json[0])
    # 深度递归遍历转换数据
    trans_root = _dfs_topic(xmind_root_topic, time_stamp)

    return {
        "template": template,
        "root": trans_root,
        "theme": theme,
        "version": version,
        "base": base
    }


# 转换成生成xmind数据格式
def _dfs_db_json(db_json):
    if not db_json:
        return
    topic = {
        'title': db_json.get('data').get('text')
    }
    children = db_json.get('children')
    if len(children) > 0:
        topic_children = []
        for item in children:
            topic_children.append(_dfs_db_json(item))
        topic['topics'] = topic_children
    return topic


def prase_xmind(db_json, topic_structure="org.xmind.ui.logic.right"):
    root_topic = _dfs_db_json(db_json.get('root'))
    xmind_root = [{
        'topic': root_topic,
        'structure': topic_structure
    }]
    return xmind_root


def listToJson(lst):
    import json
    import numpy as np
    print(np.arange(len(lst)))
    keys = [str(x) for x in np.arange(len(lst))]
    print(keys)
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=4, ensure_ascii=False)  # json转为string
    return str_json


def get_random_str():
    uuid_val = uuid.uuid4()
    # 获取uuid的随机数字符串
    uuid_str = str(uuid_val).encode('utf-8')
    # 获取md5实例
    md5 = hashlib.md5()
    # 拿取uuid的md5摘要
    md5.update(uuid_str)
    # 返回固定长度的字符串
    return md5.hexdigest()

def make_xmind(parent_node, topic_data):
    """
    根据topic数据生成xmind内容
    :param parent_node: topic所在的节点
    :param topic_data: topic数据
    :return:
    """
    node = parent_node.addSubTopic()
    for key in topic_data:
        if key == 'title':
            node.setTitle(topic_data['title'])
        elif key == 'structure':
            node.setStructureClass(topic_data['structure'])
        elif key == 'topic':
            make_xmind(node, topic_data['topic'])
        elif key == 'topics':
            if isinstance(topic_data['topics'], list):
                for i in range(len(topic_data['topics'])):
                    make_xmind(node, topic_data['topics'][i])

def make_xmind(parent_node, topic_data):
    """
    根据topic数据生成xmind内容
    :param parent_node: topic所在的节点
    :param topic_data: topic数据
    :return:
    """
    node = parent_node.addSubTopic()
    for key in topic_data:
        if key == 'title':
            node.setTitle(topic_data['title'])
        elif key == 'structure':
            node.setStructureClass(topic_data['structure'])
        elif key == 'topic':
            make_xmind(node, topic_data['topic'])
        elif key == 'topics':
            if isinstance(topic_data['topics'], list):
                for i in range(len(topic_data['topics'])):
                    make_xmind(node, topic_data['topics'][i])


if __name__ == '__main__':

    # 测试数据，需要确保测试数据是arry类型，同时长度大于等于1
    # test_data = [{'title': '画布 1', 'topic': {'title': '2.0', 'topics': [{'title': '基础配置', 'topics': [{'title': '反向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '正向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '交割', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}]}, {'title': '交易下单缓存', 'topics': [{'title': '反向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '正向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '交割', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}]}]}, 'structure': 'org.xmind.ui.map.unbalanced'}]
    # # 调用转换函数
    # # str_data = test_data.join(test_data)
    # # print(str_data)
    # trans_result = trans_xmind(test_data)
    # result_data = json.dumps(trans_result,ensure_ascii=False)
    # print(result_data)
    # # genXmind(str_data)
    # print(genXmind())

    # 生成xmind数据
    test_data = {"template": "right", "root": {"data": {"created": 1647418166263, "text": "2.0", "id": "657891fc-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "基础配置", "id": "657892c4-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "反向永续", "id": "657892f6-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "限价单", "id": "65789314-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "市价单", "id": "6578933c-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "条件单", "id": "6578935a-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "方式", "id": "65789378-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "GTC", "id": "65789396-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "IOC", "id": "657893be-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "FOK", "id": "657893dc-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "被动委托", "id": "657893fa-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "触发后平仓", "id": "6578940e-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}]}]}, {"data": {"created": 1647418166263, "text": "正向永续", "id": "6578942c-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "限价单", "id": "6578945e-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "市价单", "id": "65789486-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "条件单", "id": "657894a4-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "方式", "id": "657894c2-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "GTC", "id": "657894e0-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "IOC", "id": "657894f4-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "FOK", "id": "65789512-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "被动委托", "id": "6578953a-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "触发后平仓", "id": "65789558-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}]}]}, {"data": {"created": 1647418166263, "text": "交割", "id": "65789576-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "限价单", "id": "65789594-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "市价单", "id": "657895a8-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "条件单", "id": "657895c6-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "方式", "id": "657895e4-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "GTC", "id": "65789602-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "IOC", "id": "65789616-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "FOK", "id": "65789634-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "被动委托", "id": "65789652-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "触发后平仓", "id": "65789670-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}]}]}]}, {"data": {"created": 1647418166263, "text": "交易下单缓存", "id": "6578968e-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "反向永续", "id": "657896c0-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "限价单", "id": "657896de-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "市价单", "id": "657896fc-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "条件单", "id": "65789724-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "方式", "id": "65789742-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "GTC", "id": "65789756-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "IOC", "id": "65789774-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "FOK", "id": "65789792-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "被动委托", "id": "657897b0-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "触发后平仓", "id": "657897c4-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}]}]}, {"data": {"created": 1647418166263, "text": "正向永续", "id": "657897f6-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "限价单", "id": "65789814-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "市价单", "id": "65789828-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "条件单", "id": "65789846-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "方式", "id": "65789864-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "GTC", "id": "65789882-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "IOC", "id": "65789896-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "FOK", "id": "657898b4-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "被动委托", "id": "65789aa8-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "触发后平仓", "id": "65789ac6-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}]}]}, {"data": {"created": 1647418166263, "text": "交割", "id": "65789ae4-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "限价单", "id": "65789b16-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "市价单", "id": "65789b2a-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "条件单", "id": "65789b48-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "方式", "id": "65789b70-a500-11ec-8de6-0a5b554c9c4e"}, "children": [{"data": {"created": 1647418166263, "text": "GTC", "id": "65789b8e-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "IOC", "id": "65789bac-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "FOK", "id": "65789bca-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "被动委托", "id": "65789be8-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}, {"data": {"created": 1647418166263, "text": "触发后平仓", "id": "65789bfc-a500-11ec-8de6-0a5b554c9c4e"}, "children": []}]}]}]}]}, "theme": "fresh-blue", "version": "1.4.43", "base": 16}
    # print(json.dumps(test_data, indent=4, ensure_ascii=False))
    xmind_data = prase_xmind(test_data)
    print(type(xmind_data))
    # print(json.dumps(xmind_data, indent=4, ensure_ascii=False))
    print(type(json.dumps(xmind_data, indent=4, ensure_ascii=False)))
    #
    root_topic_list = [{'topic': {'title': '2.0', 'topics': [{'title': '基础配置', 'topics': [{'title': '反向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '正向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '交割', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}]}, {'title': '交易下单缓存', 'topics': [{'title': '反向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '正向永续', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}, {'title': '交割', 'topics': [{'title': '限价单'}, {'title': '市价单'}, {'title': '条件单'}, {'title': '方式', 'topics': [{'title': 'GTC'}, {'title': 'IOC'}, {'title': 'FOK'}, {'title': '被动委托'}, {'title': '触发后平仓'}]}]}]}]}, 'structure': 'org.xmind.ui.map.unbalanced'}]
    root_topic = root_topic_list[0]['topic']

    workbook = xmind.load("temp.xmind")
    sheet = workbook.getPrimarySheet()

    # 设置根节点
    root_node = sheet.getRootTopic()
    root_node.setTitle(root_topic['title'])

    # 设置子节点
    for work_item in root_topic['topics']:
        make_xmind(root_node, work_item)

    xmind.save(workbook, path='sample.xmind')


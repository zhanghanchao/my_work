# -*-coding:utf-8-*-
# 文件操作步骤
# 1,打开文件
# r+表示可读写，增加内容
# w+表示会清空再写入,可创建新文件，
# a+会在末尾的位置追加数据，不清空原来的内容
f = open("data.txt", 'r', encoding='utf-8')
# 2,操作文件：读/写内容
# print(f.read())
result = f.read()
print(type(result))
print(result)
# 读取一次后游标发生变化
f.seek(0)
result1 = f.readlines()
# 读取一行内容
result3 = f.readline()
print(type(result1))
print(result1)
# 3,关闭文件（读写完成，要及时的关闭）
f.close()

# with关键字会在结束后自动关闭
with open("data.txt", 'w+', encoding='utf-8') as f:
    f.read()
    print(f.write('\nappend1\n'))

print(f.closed)





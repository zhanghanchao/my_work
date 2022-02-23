# -*-coding:utf-8-*-

import pymysql

# 建立链接
conn = pymysql.connect(
    host = "",
    user = "root",
    password = "",
    database = "数据库名",
    charset = "utf8mb4"
)

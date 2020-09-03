import sqlite3

# 建库
cx = sqlite3.connect("e:\\test.db")
# 建表
cu = cx.cursor()
# cu.execute("""create table catalog if not exists( id integer primary key, pid integer, name varchar(10) UNIQUE )""")

# 执行插入操作
cu.execute("insert into catalog values(0, 0, 'name1')")
cu.execute("insert into catalog values(1, 0, 'hello')")
cx.commit()

import mysql.connector

# 连接
conn = mysql.connector.connect(user='root', password='123456', database='test')

# 写入
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
conn.commit()

# 查询
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭
cursor.close()
conn.close()

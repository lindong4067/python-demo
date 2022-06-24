# -*- coding: utf-8 -*-

import os, sqlite3

# 清库
db_file = os.path.join(os.path.dirname(__file__), '../test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始化数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()


def get_score_in(low, high):
    global conn_inner, cursor_inner
    try:
        conn_inner = sqlite3.connect(db_file)
        cursor_inner = conn_inner.cursor()
        cursor_inner.execute('select * from user where score between ? and ? order by score', (low, high))
        values = cursor_inner.fetchall()
        return [v[1] for v in values]
    except:
        print('Error occurred')
    finally:
        conn_inner.commit()
        cursor_inner.close()
        conn_inner.close()


# 测试:
assert get_score_in(80, 95) == ['Adam']
print(get_score_in(80, 95))
assert get_score_in(60, 80) == ['Bart', 'Lisa']
print(get_score_in(60, 80))
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam']
print(get_score_in(60, 100))

print('Pass')

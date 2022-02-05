import sqlite3

conn = sqlite3.connect('name.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES('hello','word')''')
d='red'
f='black'
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''',(d, f))
cursor.execute('''SELECT*FROM tab_1''')
k=cursor.fetchall()
conn.commit()
cursor.execute('''SELECT*FROM tab_1 WHERE col_1='hello' ''')
cursor.execute('''SELECT*FROM tab_1 WHERE col_2 LIKE '7%' ''')
cursor.execute('''SELECT*FROM tab_1 ORDER BY col_2 ''')
cursor.execute('''DELETE  FROM tab_1 WHERE id=1''')
conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE col_1='red' ''')
conn.commit()
cursor.execute(''' SELECT*FROM tab_1''')
conn.commit()
k=cursor.fetchall()
print(k)

# conn = sqlite3.connect('name2.db')
# cursor = conn.cursor()
# d='red'
# f='black'
# a=int(input())
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,
# col_2 TEXT, col_3 TEXT)''')
# cursor.execute('''INSERT INTO tab_2(col_1,col_2,col_3) VALUES('hello','word','a')''')
# conn.commit()



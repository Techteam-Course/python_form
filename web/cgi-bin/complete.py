#! /usr/bin/env python3

import cgi
import os
import sys
import io
import sqlite3

# データベースに接続する
form = cgi.FieldStorage()
student_id = form['student_id'].value
your_name = form['your_name'].value
age = form['age'].value
bikou = form['bikou'].value

con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute(
'''CREATE TABLE IF NOT EXISTS users(student_id real, your_name text, age text, bikou text)''')

sql = 'insert into users (student_id, your_name, age, bikou) values (?,?,?,?)'
user = (f'{student_id}', f'{your_name}', f'{age},', f'{bikou}')
cur.execute(sql, user)

con.commit()

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print('Content-type: text/html;charset=utf-8')

# htmlの部分
print(
    """
    <html>
      <head>
          <meta http-equiv=\”Content-Type\” content=\ “text/html
          charset=utf-8\” / >
      </head>
    <body>
      <p>登録が完了しました。<P>
      <a href='http://localhost:8000/cgi-bin/index.py'>TOPへ戻る</a>
    </body>
    """
)

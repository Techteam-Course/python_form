#! /usr/bin/env python3
import sys
import io
import sqlite3

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# データベースに接続する
con = sqlite3.connect('example.db')
cur = con.cursor()

student_list = """<h1>リスト</h1>"""

# レコードを生年月日の降順で取得する
for row in cur.execute('SELECT * FROM users ORDER BY student_id DESC'):
    a = """<p>学籍番号:{0[0]}\n氏名:{0[1]}\n年齢:{0[2]}\n備考:{0[3]}</p>""".format(row)
    student_list = student_list + a

# データベースとの接続を終了
con.close()

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print('Content-type:text/html;charset=utf-8')

print("""
    <html>
      <head>
          <meta http-equiv=\”Content-Type\” content=\ “text/html
          charset=utf-8\” / >
      </head>
    <body>
        <form name="registration" method="GET" action="http://localhost:8000/main.html">
            <input type="submit" value="登録はこちら" name="registration">
        </form>
      """ + student_list + """ </body>
    """)

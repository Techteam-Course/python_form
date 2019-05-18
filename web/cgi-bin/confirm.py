#!/usr/bin/env python3

import cgi
import sys
import io


# 日本語を受信時にエラーにならないようにする為に必要。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

your_name = form.getfirst('your_name')
student_id = form.getfirst('student_id')
age = form.getfirst('age')
bikou = form.getfirst('bikou')


# テキストファイルとして内容を出力
li = {'student_id': student_id, 'your_name': your_name, 'age': age, 'bikou': bikou}

print("Content-type: text/html; charset=utf-8")

print(
    """
    <html>
    <head>
        <meta http-equiv=\”Content-Type\” content=\ “text/html
        charset=utf-8\” / >
    </head>
    <body>
        <p>お名前:{0[your_name]}</p>
        <p>学籍番号:{0[student_id]}</p>
        <p>年齢:{0[age]}</p>
        <p>備考:{0[bikou]}</p>
        <p>以上の内容で登録しますか</p>
        <p>登録される場合はokを押してください</p>
        <a href="http://localhost:8000/cgi-bin/complete.py?student_id={0[student_id]}&your_name={0[your_name]}&age={0[age]}&bikou={0[bikou]}">ok</a>
    </body>
    """.format(li)
)

#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import cgi
import sys
import io
import time
from string import Template
from os import path
import re


# 日本語を受信時にエラーにならないようにする為に必要。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

your_name = form.getfirst('your_name')
student_id = form.getfirst('student_id')
age = form.getfirst('age')
bikou = form.getfirst('bikou')

 # 入力チェック（必要な変数が送信されていない場合はエラー。）
if 'your_name' not in form:
    print('Content-type: text/html; charset=UTF-8')
    print('')
    print('名前が入力されていません')
    sys.exit()

if 'student_id' not in form:
    print('Content-type: text/html; charset=UTF-8')
    print('')
    print('学籍番号が入力されていません')
    sys.exit()

#半角数字
digitReg = re.compile(r'^[0-9]+$')
def isdigit(s):
    return digitReg.match(s) is not None

if isdigit(student_id):
    print('Content-type: text/html; charset=UTF-8')
    print('')  
    pass
else:
    print('Content-type: text/html; charset=UTF-8')
    print('')
    print('学籍番号は半角数字で入力してください')
    sys.exit()


# テキストファイルとして内容を出力
li = {'student_id': student_id, 'your_name': your_name, 'age': age, 'bikou': bikou}

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
        <a href='http://localhost:8000/cgi-bin/complete.py?student_id={0[student_id]}&your_name={0[your_name]}&age={0[age]}&bikou={0[bikou]}'>ok</a>
     </body>
     """.format(li)
)

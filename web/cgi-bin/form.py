#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import io
import sys
import cgi
import cgitb

cgitb.enable()
sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer,encoding='utf-8')

form = cgi.FieldStorage()

number = form.getvalue('number')
name = form.getvalue('name')
age = form.getvalue('age')
note = form.getvalue('note')

html_body="""
<!DOCTYPE html>
<html lang="jp">
<head>
<meta charset="utf-8">
<title>学生情報</title>
</head>

<body>
<table border="1">
    <tr>
        <th>学籍番号</th><th>名前</th><th>年齢</th><th>備考</th>
    </tr>
    <tr>
        <td>%s</td><td>%s</td><td>%s</td><td>%s</td>
    </tr>
</table>

<a href="http://localhost:8000/main.html">入力フォームへ</a>
</body>
</html>"""

print("Content-Type: text/html;charset=utf-8")
print()
print(html_body % (number,name,age,note))
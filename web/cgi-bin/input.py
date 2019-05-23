#!/usr/bin/env python3

import cgi
import sys
import io


# 日本語を受信時にエラーにならないようにする為に必要。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-type: text/html; charset=utf-8")

print(
"""
<!DOCTYPE html>
<html lang="jp">
<head>
<meta charset="utf-8">
<title>学生入力フォーム</title>
</head>

<body>
<h1>学生入力フォーム</h1>
<form name="form" method="POST" action="confirm.py">
    <h3>学籍番号</h3>
        <input type="text" name="student_id" placeholder="半角数字" pattern="^[0-9]+$" required>
        ＊必須項目、半角数字
    <br>
    <h3>名前</h3>
        <input type="text" name="your_name" required>
        ＊必須項目
    <br>
    <h3>年齢</h3>
        <select name="age" required>
            <option value="" disabled selected required>選択してください</option>
            <option value="18">18</option>
            <option value="19">19</option>
            <option value="20">20</option>
            <option value="21">21</option>
            <option value="22">22</option>
            <option value="23">23</option>
            <option value="24">24</option>
            <option value="25">25</option>
            <option value="26">26</option>
            <option value="27">27</option>
        </select>
    <br>
    <h3>備考欄</h3>
        <textarea name="bikou"></textarea>
    <br>
    <input type="submit" value="送信" name="button">
</form>
</body>
</html>
"""
)
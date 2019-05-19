import django.http
import myApp.models
import myApp.forms
from django.shortcuts import render
import uuid
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate, login as django_login

def has_digit(text):
    if re.search("\d", text):
        return True
    return False

def has_alphabet(text):
    if re.search("[a-zA-Z]", text):
        return True
    return False


def post_new_post(request):
    if request.method == 'POST':
        form = myApp.forms.InputForm(request.POST)
        if form.is_valid():
            myApp.models.Post.objects.create(name=request.POST['name'], age=request.POST['age'], comment=request.POST['comment'])
            return django.http.HttpResponseRedirect('/list')
    else:
        form = myApp.forms.InputForm()
    return render(request, 'post_new_post.html', {'form': form})

def list(request):
    posts = myApp.models.Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def login_user(request):
    if request.method == 'POST':
        login_form = myApp.forms.LoginForm(request.POST)
        username = login_form.username
        password = login_form.password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return django.http.HttpResponseRedirect('/new_post')
        else:
            login_form.add_error(None, "ユーザー名またはパスワードが異なります。")
            return render(request, 'login.html', {'login_form': login_form})
        return render(request, 'login.html', {'login_form': login_form})
    else:
        login_form = myApp.forms.LoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    #アカウントとパスワードが合致したら、その人専用の投稿画面に遷移する
    #アカウントとパスワードが合致しなかったら、エラーメッセージ付きのログイン画面に遷移する


def registation_user(request):
    if request.method == 'POST':
        registration_form = myApp.forms.RegistrationForm(request.POST)
        password = request.POST['password']
        if len(password) < 8:
            registration_form.add_error('password', "文字数が8文字未満です。")
        if not has_digit(password):
            registration_form.add_error('password',"数字が含まれていません")
        if not has_alphabet(password):
            registration_form.add_error('password',"アルファベットが含まれていません")
        if registration_form.has_error('password'):
            return render(request, 'registration.html', {'registration_form': registration_form})
        user = User.objects.create_user(username=request.POST['username'], password=password, email=request.POST['email'])
        return django.http.HttpResponseRedirect('/login')
    else:
        registration_form = myApp.forms.RegistrationForm()
    return render(request, 'registration.html', {'registration_form': registration_form})

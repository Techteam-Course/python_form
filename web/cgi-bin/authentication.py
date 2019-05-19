#!/usr/bin/env python
# coding: utf-8

import sys
import io
"""

from SimpleAppServer import expose, test
from httphandler import Response
from simpletemplate import SimpleTemplate

from validators import NotEmpty, RegexValidator
from widgets import Text, Submit, Form

editforms=(Text('username', u'ユーザ名',
            validators=(NotEmpty(), RegexValidator(r'[A-Za-z\d]')),),
           Text('password', u'パスワード',
            validators=(NotEmpty(), RegexValidator(r'[A-Za-z\d]')),),
           Submit('submit', u'ログイン'))
loginform=Form(editforms, {'action':'/login', 'method':'POST'})

base_body="""<html><body>{}</body></html>""".format("test")
"""


# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")

# htmlの部分。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
print(
   """
     <html>
       <head>
           <meta http-equiv=\"Content-Type\" content=\ "text/html
           charset=utf-8\" / >
       </head>
     <body>
       Hello!! World!!
     </body>
     """
)



"""
@expose
def login_form(_request, values={}, errors={}):
    body=base_body % ('${form.display(values, errors)}')
    res=Response()
    t=SimpleTemplate(body)
    values['password']=''
    body=t.render({'form':loginform, 'values':values, 'errors':errors})
    res.set_body(body)
    return res


from Cookie import SimpleCookie
import md5
fixeduser='user'                 # (4)
fixedpass='pass'

@expose
def login(_request, username='', password=''):
    res=Response()
    values, errors=loginform.validate({'username':username,
                                       'password':password})
    if errors or fixeduser!=username or fixedpass!=password:
        return login_form(_request, values, errors)   # (1)

    c=SimpleCookie()
    m=md5.md5(username+':'+password)                  # (2)
    c['authhash']=m.hexdigest()                       # (3)
    c['authhash']['expires']='Thu, 1-Jan-2030 00:00:00 GMT'
    res.set_header(*c.output().split(': '))
    res.status=302
    res.set_header('Location', '/')
    res.set_body('')
    return res


@expose
def logout(_request):
    body=base_body % ('<p>Logged out</p>')
    res=Response()
    c=SimpleCookie()
    c['authhash']=''
    res.set_header(*c.output().split(': '))
    res.set_body(body)
    return res
"""

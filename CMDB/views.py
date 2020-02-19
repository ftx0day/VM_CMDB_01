from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models
from . import forms
def index(request):
    pass
    return render(request, 'CMDB/index.html')



def login(request):

    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/CMDB/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)

            except :
                message = '用户不存在！'
                return render(request, 'CMDB/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/CMDB/')
            else:
                message = '密码不正确！'
                return render(request, 'CMDB/login.html',locals())
        else:
            return render(request, 'CMDB/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'CMDB/login.html', locals())

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'CMDB/index.html')
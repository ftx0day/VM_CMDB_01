from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def index(request):
    pass
    return render(request, 'CMDB/index.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        return redirect('/CMDB/')
    return render(request, 'CMDB/login.html')
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('blog:post_list')
    
    context = {
        'loginform': form
    }

    return render(request,'blog/my-login.html')

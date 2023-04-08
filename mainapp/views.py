from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *

def index(request):
    ice_creams = IceCream.objects.all()
    context = {
        'title': '',
        'ice_creams': ice_creams,
    }
    return render(request, 'index.html', context = context )


def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {'form': UserForm,
                       'error': 'Неверный email или пароль'}
            return render(request, 'signin.html', context)
    context = {'form': UserForm}

    return render(request, 'signin.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def registration(request):
    form = CustomUserCreationForm()
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('index')
    context = {'form': form}
    return render(request, 'signup.html', context)



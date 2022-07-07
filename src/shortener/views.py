from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def index(request):
    return render(request, 'shortener/index.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('shortener:index')
        messages.error(request, 'Что-то пошло не так!')
    form = UserCreationForm
    return render(request, 'shortener/register.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из своей учётной записи.')
    return redirect('shortener:index')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Вы вошли под ником {username}')
                return redirect('shortener:index')
            else:
                messages.error(request, 'Что-то пошло не так')
        else:
            messages.error(request, 'Что-то пошло не так 2')
    form = AuthenticationForm
    return render(request, 'shortener/login.html', {'form': form})

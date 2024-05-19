from django.http import HttpRequest

from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def index(request: HttpRequest):
    tasks = Task.objects.all()
    print(request.user.username)
    return render(request, 'main/index.html', {'title': 'Главная стрвница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def sign_up(request: HttpRequest):
    form = CreateUserForm()

    # Проверяем отправляем ли мы форму (POST) или просто рендерим страницу
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        # валидируем форму
        if form.is_valid():
            # если форму нормально провалидирована, то сохраняем значения
            form.save()
            # получаем поля из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # ищем пользователя по этим поляем
            user = authenticate(request, username=username, password=password)

            # если нашли, то лоигинимся
            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'auth/register.html', {
        'form': form
    })

def sign_in(request):
    if request.method == 'POST':
        # Get the username and password from the request
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If the user is authenticated, log them in and redirect to the home page
        if user is not None:
            login(request, user)
            return redirect('home')

        # If the user is not authenticated, show an error message
        else:
            error_message = 'Invalid username or password'
            return render(request, 'auth/login.html', {'error_message': error_message})

    # If the request is not a POST request, show the login page
    else:
        return render(request, 'auth/login.html')
    
def logout(request: HttpRequest):
    auth_logout(request)
    return redirect('login')
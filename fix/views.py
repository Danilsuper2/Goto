from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from fix.models import Problem, Like

# Create your models here.

def like(request):
    problem = Problem.objects.get(pk=request.GET['id'])
    try:
        like = Like.objects.get(problem=problem, user=request.user)
        if like.type != int(request.GET['like']):
            like.type = request.GET['like']
            like.save()
            messages.success(request, "Лайк изменён!")
        else:
            messages.error(request, 'Вы уже поставили Лайк!')
    except:
        like = Like(problem=problem, user=request.user, type = int(request.GET['like']))
        like.save()
        messages.success(request, "Лайк добавлен")
    return redirect('/fix')


def main(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            problems = list(Problem.objects.all())
            return render(request, "main.html", {'username': request.user.username, 'list': problems})
        else:
            return redirect('/fix/login')
    else:
        logout(request)
        return redirect('/fix/login')


def log_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/fix/')
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' or password == '':
            messages.error(request, 'Заполните все поля!')
            return HttpResponse("Заполните все поля")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/fix')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('/fix/login')


def reg(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/fix/')
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' or password == '':
            messages.error(request, "Заполните все поля")
            return redirect('/fix/reg')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Логин занят")
            return redirect('/fix/reg')

        # создаем пользователя
        user = User.objects.create_user(username, password=password)
        user.save()

        # "входим" пользователя
        login(request, user)

        return redirect('/fix/')

def cab(request):
    if request.method == 'GET':
        problems = list(request.user.problem_set.all())
        return render(request, 'cab.html', {'list': problems})
    else:
        problem = Problem()
        problem.name = request.POST['name']
        problem.text_in = request.POST['text']
        problem.location = request.POST['location']
        problem.user_id = request.user.id
        problem.save()
        messages.success(request, "Новая проблема добавлена")
        return redirect('/fix/')
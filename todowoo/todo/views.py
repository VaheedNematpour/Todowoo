from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todos


def current(request):
    todos = Todos.objects.filter(user=request.user, completed=False)
    
    return render(request, 'todo/current.html', {
        'todos': todos
    })


def create(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html')
    else:
        try:
            todos = Todos()
            todos.title = request.POST.get('title')
            todos.memo = request.POST.get('memo')
            todos.important = bool(request.POST.get('important'))
            todos.user = request.user
            todos.save()
            return redirect('todo:current')
        except ValueError:
            return render(request, 'todo/create.html', {
                'error': 'Bad data entered!'
            })


def complete(request, id):
    if request.method == 'POST':
        todo = get_object_or_404(Todos, pk=id, user=request.user)
        todo.completed = 'True'
        return redirect('todo:completed')


def completed(request):
    todos = Todos.objects.filter(user=request.user, completed=True)
    
    return render(request, 'todo/completed.html', {
        'todos': todos
    })


def details(request, id):
    todo = get_object_or_404(Todos, pk=id, user=request.user)
    
    if request.method == 'GET':
        return render(request, 'todo/details.html', {
            'todo': todo
        })
    elif request.method == 'POST':
        new_todo = Todos()
        new_todo.title = request.POST.get('title')
        new_todo.memo = request.POST.get('memo')
        new_todo.important = bool(request.POST.get('important'))
        new_todo.user = request.user
        new_todo.save()
        todo.delete()
        return redirect('todo:current')


def delete(request, id):
    if request.method == 'POST':
        todo = get_object_or_404(Todos, pk=id, user=request.user)
        todo.delete()
        return redirect('todo:current')


def home(request):
    return render(request, 'todo/index.html')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todo:home')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html')
    else:
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return render(request, 'todo/login.html', {
                'error': 'The username or password is wrong!'
            })
        else:
            login(request, user)
            return redirect('todo:home')


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html')
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(
                    request.POST.get('username'),
                    password=request.POST.get('password1')
                )
                user.save()
                login(request, user)
                return redirect('todo:home')
            except IntegrityError:
                return render(request, 'todo/signup.html', {
                    'error': 'The username is already taken!'
                })
        else:
            return render(request, 'todo/signup.html', {
                'error': 'The username doesn\'t match!'
            })


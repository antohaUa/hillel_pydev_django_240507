from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/')
        else:
            context['error'] = 'Invalid username or password'
    return render(request, 'login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('/login/')


def root_page(request):
    return redirect('/login/')


def register_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        return redirect('/login/')
    return render(request, 'register.html')


@login_required()
def user_page(request):
    context = {'username': request.user.username, 'email': request.user.email, 'first_name': request.user.first_name,
               'last_name': request.user.last_name}
    return render(request, 'user.html', context=context)

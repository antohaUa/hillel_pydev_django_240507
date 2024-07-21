from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm


def login_page(request):
    """Login handler."""
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/user/')
        context['error'] = 'Invalid username or password'
    context['form'] = LoginForm()
    return render(request, 'login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('/login/')


def root_page(request):
    return redirect('/post_machine/')


def register_page(request):
    """Register new user handler."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'], email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            user.save()
        return redirect('/login/')
    return render(request, 'register.html', context={'form': RegisterForm()})


@login_required()
def user_page(request):
    if request.method == 'POST':
        user_data = User.objects.get(pk=request.user.id)
        user_data.username = request.POST['username']
        user_data.email = request.POST['email']
        user_data.first_name = request.POST['first_name']
        user_data.last_name = request.POST['last_name']
        if new_pass := request.POST['password']:
            user_data.set_password(new_pass)
        user_data.save(update_fields=['username', 'password', 'email', 'first_name', 'last_name'])
        return redirect('/user/')

    context = {'username': request.user.username, 'email': request.user.email, 'first_name': request.user.first_name,
               'last_name': request.user.last_name}
    return render(request, 'user.html', context=context)

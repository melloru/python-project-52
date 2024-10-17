from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def index(request):
    return render(request, "task_manager/index.html")


def all_users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "task_manager/users.html", context=context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы залогинены")
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "task_manager/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "Вы разлогинены")
    return redirect("index")


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect("index")
    else:
        form = RegistrationForm()
    return render(request, "task_manager/registration.html", {"form": form})

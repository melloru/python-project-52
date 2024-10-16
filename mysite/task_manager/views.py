from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView
# from .models import Users
from .models import Users
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout

def index(request):
    return render(request, "task_manager/index.html")


def all_users(request):
    users = Users.objects.all()
    context = {"users": users}
    return render(request, "task_manager/users.html", context=context)

# class User(ListView):
#     model = Users



def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы залогинены")
            redirect("index")
    else:
        form = LoginForm()
    return render(request, "task_manager/login.html", {"form": form})


def registration(request):
    try:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Пользователь успешно зарегистрирован")
                return redirect("index")
            else:
                messages.error(request, "error!")
        else:
            form = RegistrationForm()
        return render(request, "task_manager/registration.html", {"form": form})
    except Exception as e:
        print(f"Ошибка: {e}")



# def registration(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Users.objects.create(
#             #     name=form.cleaned_data['name'],
#             #     surname=form.cleaned_data['surname'],
#             #     nickname=form.cleaned_data['nickname'],
#             #     password=form.cleaned_data['password1']
#             # )
#             user = form.save(commit=False)
#             user.password = form.cleaned_data['password1']
#             user.save()
#             redirect("index")
#     else:
#         form = RegistrationForm()
#     return render(request, "task_manager/registration.html", {"form": form})

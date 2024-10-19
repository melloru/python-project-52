from django.contrib.auth.views import LoginView, LogoutView
from django.db.transaction import on_commit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Status, Tag, Task
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import RegistrationForm, LoginForm, TagForm, StatusForm
from django.contrib import messages
from django.contrib.auth import login, logout


def index(request):
    """Главная страница"""
    return render(request, "task_manager/index.html")


class Users(ListView):
    """Вывод списка пользователей"""
    model = User
    template_name = "task_manager/users.html"
    context_object_name = "users"


class UserLogin(LoginView):
    template_name = "task_manager/auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, "Вы залогинены")
        return redirect("index")


def user_logout(request):
    """Выход из аккаунта пользователя"""
    logout(request)
    messages.info(request, "Вы разлогинены")
    return redirect("index")


def registration(request):
    """Форма для регистрации пользователя"""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect("index")
    else:
        form = RegistrationForm()
    return render(request, "task_manager/auth/registration.html", {"form": form})


class Statuses(ListView):
    model = Status
    template_name = "task_manager/status/statuses.html"
    context_object_name = "statuses"


class UpdateStatus(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "task_manager/status/update.html"



def update_status(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('statuses')
    else:
        form = StatusForm()
    return render(request, "task_manager/status/update.html", {"form": form})

def delete_status(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    if request.method == "POST":
        status.delete()
        return redirect("statuses")
    return render(request, "task_manager/status/delete.html", {"status": status})

def create_status(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            new_status = Status(name=form.cleaned_data['name'])
            new_status.save()
            return redirect('statuses')
    else:
        form = StatusForm()
    return render(request, "task_manager/create.html", {"form": form})


class Tags(ListView):
    model = Tag
    template_name = "task_manager/tag/tags.html"
    context_object_name = "tags"


def update_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag.name = form.cleaned_data['name']
            tag.save()
            return redirect('tags')
    else:
        form = TagForm()
    return render(request, "task_manager/tag/update.html", {"form": form})


def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    if request.method == "POST":
        tag.delete()
        return redirect("tags")
    return render(request, "task_manager/tag/delete.html", {"tag": tag})

def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = Tag(name=form.cleaned_data['name'])
            new_tag.save()
            return redirect('tags')
    else:
        form = TagForm()
    return render(request, "task_manager/create.html", {"form": form})

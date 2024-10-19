from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Status, Tag
from .base_forms import BaseNameForm
import re


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}),
        help_text="Ваш пароль должен содержать как минимум 3 символа.")
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Подтверждение пароля"}),
        help_text="Для подтверждения введите, пожалуйста, пароль ещё раз.")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя пользователя"}),
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 3:
            raise ValidationError("Пароль должен содержать как минимум 3 символа.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError("Введенные пароли не совпадают.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
        username = forms.CharField(
            label="Имя пользователя",
            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя пользователя"}))
        password = forms.CharField(
            label="Пароль",
            widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))


class StatusForm(BaseNameForm):
    class Meta(BaseNameForm.Meta):
        model = Status

class TagForm(BaseNameForm):
    class Meta(BaseNameForm.Meta):
        model = Tag
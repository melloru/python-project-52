from django import forms
from django.forms import EmailField

from .models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class RegistrationForm(forms.Form):
#     name = forms.CharField(max_length=150, label="Имя", widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "Имя"}))
#
#     surname = forms.CharField(max_length=150, label="Фамилия", widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "Фамилия"}))
#
#     nickname = forms.CharField(max_length=150, label="Имя пользователя", widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "Имя пользователя"}),
#                                help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.")
#
#     password1 = forms.CharField(max_length=150, label="Пароль", widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "Пароль"}))
#
#     password2 = forms.CharField(max_length=150, label="Подтверждение пароля", widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "Подтверждение пароля"}))

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}))
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}))
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя пользователя"}))
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Подтверждение пароля"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 3:
            raise ValidationError("Пароль должен содержать как минимум 3 символа.")
        return password1


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают.")


# class RegistrationForm(forms.ModelForm):
#
#     password1 = forms.CharField(
#         max_length=150,
#         label="Пароль",
#         widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"})
#     )
#
#     password2 = forms.CharField(
#         max_length=150,
#         label="Подтверждение пароля",
#         widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Подтверждение пароля"})
#     )
#
#     class Meta:
#         model = Users
#         fields = ["name", "surname", "nickname"]
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
#             "surname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
#             "nickname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя пользователя"}),
#         }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя пользователя"}))
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))

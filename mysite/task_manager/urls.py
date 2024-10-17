from django.urls import path

from .views import index, all_users, user_login, registration, user_logout

urlpatterns = [
    path("", index, name="index"),
    path("users/", all_users, name="all_users"),
    path("login/", user_login, name="login"),
    path("users/create/", registration, name="registration"),
    path("logout/", user_logout, name="logout")
]

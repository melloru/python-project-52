from django.urls import path

from .views import (index, registration, user_logout, Users, UserLogin, Statuses, Tags,
                    update_status, delete_status, create_status,
                    update_tag, delete_tag, create_tag, UpdateStatus)
try:
    urlpatterns = [
        path("", index, name="index"),
        path("users/", Users.as_view(), name="users"),
        path("login/", UserLogin.as_view(), name="login"),
        path("users/create/", registration, name="registration"),
        path("logout/", user_logout, name="logout"),
        path("statuses/", Statuses.as_view(), name="statuses"),
        path("statuses/<int:pk>/update/", UpdateStatus.as_view(), name="update_status"),
        path("statuses/<int:status_id>/delete/", delete_status, name="delete_status"),
        path("statuses/create/", create_status, name="create_status"),
        path("tags/", Tags.as_view(), name="tags"),
        path("tags/<int:tag_id>/update/", update_tag, name="update_tag"),
        path("tags/<int:tag_id>/delete/", delete_tag, name="delete_tag"),
        path("tags/create/", create_tag, name="create_tag"),
    ]
except Exception as e:
    print(f"{e}")

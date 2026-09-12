from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from users.views import userLogin, index

urlpatterns = [
    path('/', index, name="index"),
    path('login/', userLogin, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name="logout"),
]
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from users.views import userLogin, index, register, edit

urlpatterns = [
    path('', index, name="index"),
    path('login/', userLogin, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register/', register, name="register"),

    # Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"),
         name="password_change"),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name="password_change_done"),

    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/register.html"), name="register"),
    path('profile/edit/', edit, name="edit"),

]
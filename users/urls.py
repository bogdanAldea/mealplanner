from django.urls import path
from .views.menu import dashboard_view, account_view
from .views.auth import register, login, logout


app_name = 'users'

urlpatterns: list = [
    path("", dashboard_view.DashboardView, name="dashboard"),
    path("account", account_view.UserAccountView, name="account"),
    path("register/", register.RegisterUserView, name="register"),
    path("login/", login.LoginUserView, name="login"),
    path("logout/", logout.LogoutUserView, name="logout"),
]
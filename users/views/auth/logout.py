from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def LogoutUserView(request):
    """View function that logs out the current logged user out of his account.
    Once logged out, the user is redirected to the login page of the
    application."""

    logout(request)
    return redirect("users:login")
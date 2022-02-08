from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def LoginUserView(request):
    """Defined view function that executes an attempted authentication
    by a user. Once the user is successfully authenticated, will be
    redirected to a main page (the dashboard page)."""

    if request.method == "POST":
        username: str = request.POST.get("username")
        password: str = request.POST.get("password")

        existing_user = authenticate(request, username=username, password=password)

        if existing_user is not None:
            login(request, existing_user)
            return redirect("users:dashboard")

    return render(request, "users/pages/login_user.html")
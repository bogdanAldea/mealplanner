from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def UserAccountView(request):
    return render(request, "users/menu/account_view.html")
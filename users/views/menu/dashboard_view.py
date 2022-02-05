from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="users:login")
def DashboardView(request):
    context = {}
    return render(request, "users/pages/dashboard.html", context)
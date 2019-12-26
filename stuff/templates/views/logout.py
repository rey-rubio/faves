from django.contrib.auth import logout as logout_user
from django.shortcuts import render


def logout(request):
    logout_user(request)
    return render(request, 'stuff/login.html')

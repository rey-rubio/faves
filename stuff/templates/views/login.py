from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    print(login.__name__)
    print(request)
    print(request.get_full_path())
    if request.method == 'POST':
        try:
            user = authenticate(email=request.POST.get('email', None), password=request.POST.get('password', None))
            if user is not None:
                login_user(request, user)
                return HttpResponseRedirect(reverse('stuff:index'))
            else:
                return HttpResponseRedirect(reverse('stuff:login_view'))

        except Exception as err:
            print(err.message)
            for i in err.message:
                print(i)

    return render(request, 'stuff/login.html')

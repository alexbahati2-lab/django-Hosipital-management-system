from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.GET.get('next', '/')  # capture next URL

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'error': "Invalid username or password"})

    # GET request
    next_url = request.GET.get('next', '/')
    return render(request, 'accounts/login.html', {'next': next_url})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm


def add(request):
    form = SignUpForm()
    context = {'form': form}

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'users/adduser.html', context)


def bulk_add(request):
    pass


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {user}.")

                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_request(request):
    '''Перенаправляет на страницу авторизации'''
    logout(request)
    print(request.POST)
    return redirect('login')






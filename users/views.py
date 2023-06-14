from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerView(request):
    """Creates a new user to the app"""
    form = CustomUserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, 'User created successfully')
        login(request, user)
        # Redirect to a success page.
        return redirect('/trainer/clients')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def loginView(request, user=None):
    if request.user.is_authenticated:
        return redirect('/trainer/clients')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/trainer/clients')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Username or password incorrect')
            form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@login_required
def logoutView(request):
    logout(request)
    return redirect('/login')
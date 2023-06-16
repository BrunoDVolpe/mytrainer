from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegisterForm, LoginForm, UserProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def homeView(request):
    context = {}
    return render(request, 'home.html', context)


def registerView(request):
    """Creates a new user to the app"""
    form = CustomUserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, 'User created successfully')
        login(request, user)
        # Redirect to a success page.
        return redirect('/profile/update')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def loginView(request, user=None):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
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


@login_required
def userProfileView(request):
    context = {}
    return render(request, 'profile.html', context)


@login_required
def userProfileUpdateView(request):
    form = UserProfileUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('profile')
    context = {
        'form': form,
    }
    return render(request, 'profile_update.html', context)
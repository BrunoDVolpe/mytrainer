from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserRegisterForm, LoginForm, UserProfileUpdateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from trainer.models import ClientProfile

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
        # Logins the user
        login(request, user)

        # Link user to a ClientProfile
        try:
            client_profile = ClientProfile.objects.get(client_email=user.email)
            client_profile.user = user
            client_profile.save()
        except:
            pass
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


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'auth/change_password.html', context)
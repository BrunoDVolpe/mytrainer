from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .forms import (CustomUserRegisterForm, LoginForm, UserProfileUpdateForm,
                     MyPasswordChangeForm, TrainerProfileUpdateForm)
from trainer.models import ClientProfile, TrainerProfile

# Create your views here.
def homeView(request):
    """Renders the homepage"""
    context = {}
    return render(request, 'home.html', context)


def registerView(request):
    """Creates a new user to the app"""
    form = CustomUserRegisterForm(request.POST or None)
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User created successfully')
            # Logins the user
            login(request, user)

            # Link user to a ClientProfile
            try:
                # Looking for client_profile created by a Personal Trainer professional
                client_profile = ClientProfile.objects.get(client_email=user.email)
                client_profile.user = user
                client_profile.save()
            except:
                pass

            # Create a Personal Trainer profile
            if form.cleaned_data['is_personal']:
                personal_group = Group.objects.get(name='personal_trainer')
                user.groups.add(personal_group)
                TrainerProfile.objects.create(user=user, name=user.email)

            # Redirect to a success page.
            return redirect('/profile/update')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def loginView(request, user=None):
    """Authenticates a user in the platform"""
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
    """Logs a user out"""
    logout(request)
    return redirect('home')


@login_required
def userProfileView(request):
    """Shows the user profile information and if the user has a trainer profile
      also shows the trainer options"""
    try:
        trainer_profile = TrainerProfile.objects.get(user=request.user)
        context = {'trainer_profile': trainer_profile}
    except:
        context = {}
    return render(request, 'profile.html', context)


@login_required
def userProfileUpdateView(request):
    """Updates user and trainer (if personal trainer professional) profile data"""
    try:
        trainer_profile = TrainerProfile.objects.get(user=request.user)
        is_trainer = True
    except:
        is_trainer = False
        trainer_profile = None

    form_user = UserProfileUpdateForm(instance=request.user)
    form_trainer = TrainerProfileUpdateForm(instance=trainer_profile)
    if request.method == 'POST':
        form_trainer = TrainerProfileUpdateForm(request.POST)
        if form_trainer.is_valid():
            trainer = TrainerProfile.objects.get(user=request.user)
            trainer.name = form_trainer.cleaned_data['name']
            trainer.save()

        form_user = UserProfileUpdateForm(request.POST)
        if form_user.is_valid():
            user = User.objects.get(id=request.user.id)
            user.first_name = form_user.cleaned_data['first_name']
            user.last_name = form_user.cleaned_data['last_name']
            user.save()
            return redirect('profile')

    context = {
        'is_trainer': is_trainer,
        'form_trainer': form_trainer,
        'form_user': form_user,
    }
    return render(request, 'profile_update.html', context)


@login_required
def changePassword(request):
    """Changes a user's password"""
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyPasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'auth/change_password.html', context)
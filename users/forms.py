from django import forms
from django.contrib.auth.models import User
from trainer.models import TrainerProfile
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError


class CustomUserRegisterForm(UserCreationForm):
    """Register's form"""
    username = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Email address',
                                        'autofocus': True}
                             ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                        'placeholder': 'Password'}
                                    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                        'placeholder': 'Confirm Password'}
                                    ))
    is_personal = forms.BooleanField(label='Personal Trainer Professional?',
                                     required=False,
                                     initial=False,
                                     widget=forms.CheckboxInput(
                                         attrs={'type': 'checkbox'})
                                     )

    def clean_username(self):
        """Prevent duplicate username and email"""
        username = self.cleaned_data['username'].lower().strip()
        new_user = User.objects.filter(username=username)

        if new_user.count():
            raise ValidationError('This email is taken. Please try another.')
        return username

    def clean_password2(self):
        """Check if both passwords were written and if they match"""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Saves the user to the database"""
        user = User.objects.create_user(
            self.cleaned_data['username'], # username input
            self.cleaned_data['username'], # email input, setting email = username
            self.cleaned_data['password1'] # password input
        )
        return user
    

class LoginForm(forms.Form):
    """Login form"""
    #email = forms.EmailField(label='Email')
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Email address',
                                        'autofocus': True}
                             ))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Password'}
                               ))


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].disabled = True


class TrainerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ['name']


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget=forms.PasswordInput(
                                attrs={"class": "form-control",
                                       'placeholder': 'Old password',
                                        'autofocus': True})
        self.fields["new_password1"].widget=forms.PasswordInput(
                                attrs={"class": "form-control",
                                       'placeholder': 'New password'})
        self.fields["new_password2"].label=''
        self.fields["new_password2"].widget=forms.PasswordInput(
                                attrs={"class": "form-control",
                                       'placeholder': 'Confirm new password'})
        
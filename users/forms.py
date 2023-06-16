from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserRegisterForm(UserCreationForm):
    """Register's form"""
    username = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    #email = username

    def clean_username(self):
        """Prevent duplicate username and email"""
        username = self.cleaned_data['username'].lower().strip()
        new_user = User.objects.filter(username=username)

        if new_user.count():
            raise ValidationError("Email Already Exist")
        return username

    def clean_password2(self):
        """Check if both passwords were written and if they match"""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit = True):
        """Saves the user to the database"""
        user = User.objects.create_user(
            self.cleaned_data['username'], # username
            self.cleaned_data['username'], # email
            self.cleaned_data['password1'] # password
        )
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].disabled = True
"""
User application forms

"""

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# TODO: replace with AuthenticationForm
class UserSignInForm(forms.Form):
    """User sign in (login) form"""

    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        self.user = authenticate(username=username, password=password)
        if self.user is None:
            raise ValidationError("incorrect username or password")


# TODO: replace with UserCreationForm
class UserSignUpForm(forms.Form):
    """User sign up (registration) form"""

    username = forms.CharField(label="username", max_length=32)
    email = forms.EmailField(label="email")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="confirm password", widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
            self.add_error("username", "username already exists")

        except User.DoesNotExist:
            return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password1", "password do not  match")
            self.add_error("password2", "password do not  match")

    def create_user(self):
        super().clean()
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password1"]
            email = self.cleaned_data["email"]
            User.objects.create_user(username, email, password)

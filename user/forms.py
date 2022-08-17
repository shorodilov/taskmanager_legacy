"""
User application forms

"""

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserSignInForm(forms.Form):
    """User sign in form"""

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

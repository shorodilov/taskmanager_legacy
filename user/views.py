"""
User application views

"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def user_detail_view(request: HttpRequest) -> HttpResponse:
    """User profile view"""

    return render(request, "user/profile.html")


def signup_view(request: HttpRequest) -> HttpResponse:
    """User signup (registration) view"""

    raise NotImplementedError()


def signin_view(request: HttpRequest) -> HttpResponse:
    """User signin (login) view"""

    raise NotImplementedError()


def logout_view(request: HttpRequest) -> HttpResponse:
    """User logout view"""

    raise NotImplementedError()

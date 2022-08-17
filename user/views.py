"""
User application views

"""

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods

from user.forms import UserSignInForm, UserSignUpForm


@login_required(login_url=reverse_lazy("user:signin"))
def user_detail_view(request: HttpRequest) -> HttpResponse:
    """User profile view"""

    return render(request, "user/profile.html")


@require_http_methods(["GET", "POST"])
def signup_view(request: HttpRequest) -> HttpResponse:
    """User signup (registration) view"""

    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.create_user()

            return HttpResponseRedirect(reverse("user:signin"))

    else:
        form = UserSignUpForm()

    return render(request, "registration/signup.html", {"form": form})


@require_http_methods(["GET", "POST"])
def signin_view(request: HttpRequest) -> HttpResponse:
    """User signin (login) view"""

    if request.method == "POST":
        form = UserSignInForm(request.POST)  # create form with data
        if form.is_valid():
            login(request, form.user)
            # noinspection PyArgumentList
            redirect_url = request.GET.get("next") or reverse("task:list")

            return HttpResponseRedirect(redirect_url)

    else:
        form = UserSignInForm()  # create an empty form

    return render(request, "registration/signin.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    """User logout view"""

    logout(request)
    return HttpResponseRedirect(reverse("task:list"))

"""
User application views

"""

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods

from user.forms import CustomizedUserChangeForm as UserChangeForm
from user.forms import UserSignInForm, UserSignUpForm


@require_http_methods(["GET"])
@login_required(login_url=reverse_lazy("user:signin"))
def user_detail_view(request: HttpRequest) -> HttpResponse:
    """User profile view"""

    ctx = {
        "user_change_form": UserChangeForm(instance=request.user),
        "password_change_form": PasswordChangeForm(user=request.user)
    }

    return render(request, "user/profile.html", ctx)


@require_http_methods(["POST"])
def user_change_view(request: HttpRequest) -> HttpResponse:
    """Change user data view"""

    form = UserChangeForm(instance=request.user, data=request.POST)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse("user:profile"))

    ctx = {
        "user_change_form": form,
        "password_change_form": PasswordChangeForm(user=request.user)
    }

    return render(request, "user/profile.html", ctx)


@require_http_methods(["POST"])
def password_change_view(request: HttpRequest) -> HttpResponse:
    """Change user password view"""

    form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse("user:profile"))

    ctx = {
        "user_change_form": UserChangeForm(instance=request.user),
        "password_change_form": form,
    }

    return render(request, "user/profile.html", ctx)


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

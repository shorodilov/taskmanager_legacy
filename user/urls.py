"""
User application URL Configuration

"""

from django.urls import path

from user import views

app_name = "user"
urlpatterns = [
    path("signin/", views.signin_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.user_detail_view, name="profile"),
]

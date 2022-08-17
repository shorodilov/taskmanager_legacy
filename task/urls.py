"""
Task application URL Config

"""

from django.urls import path

from task import views

app_name = "task"
urlpatterns = [
    path("", views.task_list_view, name="list"),
    path("<int:pk>/", views.task_detail_view, name="detail"),
]

"""
Task application URL Config

"""

from django.urls import path

from task import views

app_name = "task"
urlpatterns = [
    path("", views.task_list_view, name="list"),
    path("<int:pk>/", views.task_detail_view, name="detail"),
    path("create/", views.task_create_view, name="create"),
    path("<int:pk>/update/", views.task_update_view, name="update"),
    path("<int:pk>/delete/", views.task_delete_view, name="delete"),
]

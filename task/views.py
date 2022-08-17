"""
Task application views

"""

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from task.models import TaskModel


def task_list_view(request: HttpRequest) -> HttpResponse:
    """Task list view implementation"""

    ctx = {"object_list": TaskModel.objects.all()}
    return render(request, "task/task_list.html", ctx)


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task detail view implementation"""

    try:
        ctx = {"object": TaskModel.objects.get(pk=pk)}
        return render(request, "task/task_detail.html", ctx)
    except TaskModel.DoesNotExist:
        raise Http404("Task not found")

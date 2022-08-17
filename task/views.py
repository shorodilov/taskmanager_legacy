"""
Task application views

"""

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

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


@require_http_methods(["GET", "POST"])
def task_create_view(request: HttpRequest) -> HttpResponse:
    """Task create view implementation"""

    raise NotImplementedError()


@require_http_methods(["GET", "POST"])
def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task update view implementation"""

    raise NotImplementedError()


@require_http_methods(["GET", "POST"])
def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task delete view implementation"""

    raise NotImplementedError()

"""
Task application views

"""

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# TODO: remove this after models implementation
TASKS = {
    1: {"task_id": 1, "title": "task #1", "completed": False},
    2: {"task_id": 2, "title": "task #2", "completed": True},
    3: {"task_id": 3, "title": "task #3", "completed": False},
}


def task_list_view(request: HttpRequest) -> HttpResponse:
    """Task list view implementation"""

    ctx = {"object_list": TASKS.values()}
    return render(request, "task/task_list.html", ctx)


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task detail view implementation"""

    try:
        ctx = {"object": TASKS[pk]}
        return render(request, "task/task_detail.html", ctx)
    except KeyError:
        raise Http404("Task not found")

"""
Task application views

"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def task_list_view(request: HttpRequest) -> HttpResponse:
    """Task list view implementation"""

    return render(request, "task/task_list.html")


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task detail view implementation"""

    ctx = {"task_id": pk}
    return render(request, "task/task_detail.html", ctx)

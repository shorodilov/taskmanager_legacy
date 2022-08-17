"""
Task application views

"""
from django.http import HttpRequest, HttpResponse


def task_list_view(request: HttpRequest) -> HttpResponse:
    """Task list view implementation"""

    return HttpResponse("<h1>Task List View</h1>")


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task detail view implementation"""

    return HttpResponse(f"<h1>Task {pk} Detail View</h1>")

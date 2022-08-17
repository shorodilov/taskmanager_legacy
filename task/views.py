"""
Task application views

"""

from django.http import Http404, HttpRequest, HttpResponse, \
    HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from task.forms import TaskForm
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

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse("task:detail", args=(form.instance.pk,))

            return HttpResponseRedirect(redirect_url)

    else:
        form = TaskForm()

    return render(request, "task/task_form.html", {"form": form})


@require_http_methods(["GET", "POST"])
def task_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task update view implementation"""

    try:
        task = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        raise Http404("Task not found")

    if request.method == "POST":
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse("task:detail", args=(task.pk,))

            return HttpResponseRedirect(redirect_url)

    else:
        form = TaskForm(instance=task)

    return render(request, "task/task_form.html", {"form": form})


@require_http_methods(["GET", "POST"])
def task_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    """Task delete view implementation"""

    try:
        ctx = {"object": TaskModel.objects.get(pk=pk)}
    except TaskModel.DoesNotExist:
        raise Http404("Task not found")

    if request.method == "POST":
        ctx["object"].delete()

        return HttpResponseRedirect(reverse("task:list"))

    else:
        return render(request, "task/task_confirm_delete.html", ctx)

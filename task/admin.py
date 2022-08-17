"""
Task application administration

"""

from django.contrib import admin

from task.models import ProjectModel, TaskModel, TaskTagModel


@admin.display(description="tasks count")
def tasks_count(obj: ProjectModel | TaskTagModel) -> int:
    return obj.tasks.count()


@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = "title", "summary", tasks_count
    list_display_links = "title",  # note it is a tuple, not a string
    ordering = "title",


@admin.register(TaskTagModel)
class TaskTagModelAdmin(admin.ModelAdmin):
    list_display = "name", tasks_count
    list_display_links = "name",


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = "title", "created_at", "updated_at"
    list_display_links = "title",
    ordering = "project", "title"
    list_filter = "project", "tag"

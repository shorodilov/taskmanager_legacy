"""
Task application administration

"""

from django.contrib import admin

from task.models import ProjectModel, TaskModel, TaskTagModel


@admin.display(description="tasks count")
def tasks_count(obj: ProjectModel | TaskTagModel) -> int:
    return obj.tasks.count()


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = "title", "summary", tasks_count
    list_display_links = "title",  # note it is a tuple, not a string
    ordering = "title",


admin.site.register(ProjectModel, ProjectModelAdmin)


class TaskTagModelAdmin(admin.ModelAdmin):
    list_display = "name", tasks_count
    list_display_links = "name",


admin.site.register(TaskTagModel, TaskTagModelAdmin)


class TaskModelAdmin(admin.ModelAdmin):
    list_display = "title", "created_at", "updated_at"
    list_display_links = "title",
    ordering = "project", "title"
    list_filter = "project", "tag"


admin.site.register(TaskModel, TaskModelAdmin)

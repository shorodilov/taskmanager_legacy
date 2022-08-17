"""
Task application administration

"""

from django.contrib import admin

from task.models import ProjectModel, TaskModel, TaskTagModel

admin.site.register(ProjectModel)
admin.site.register(TaskModel)
admin.site.register(TaskTagModel)

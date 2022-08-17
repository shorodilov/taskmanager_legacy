"""
Task application forms

"""

from django import forms

from task.models import TaskModel


class TaskForm(forms.ModelForm):
    """Task form implementation"""

    class Meta:
        model = TaskModel
        fields = "title", "project", "description", "assignee"

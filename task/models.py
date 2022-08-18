"""
Task application models

"""

from django.conf import settings
from django.db import models


class ProjectModel(models.Model):
    """Project model implementation

    A project is used as a container for a group of tasks.

    :cvar id: unique project identifier, auto created by Django
    :type id: int
    :cvar title: project's title
    :type title: str
    :cvar summary: some descriptive project summary
    :type summary: str
    :cvar description: optional project detailed description
    :type description: str

    """

    class Meta:
        db_table = "project"
        verbose_name = "project"
        verbose_name_plural = "projects"

    title = models.CharField(
        max_length=32,
        verbose_name="project title",
        help_text="Required. 32 characters or fewer."
    )
    summary = models.CharField(
        max_length=128,
        verbose_name="short project description",
        help_text="Required. 128 characters or fewer."
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="detailed project description"
    )

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"<Project(pk={self.pk}, title='{self.title}')>"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.title


class TaskTagModel(models.Model):
    """Task tag model implementation

    A tag is used a marker (label) for a particular task.

    :cvar id: unique tag identifier, auto created by Django
    :type id: int
    :cvar name: tag name
    :type name: str

    """

    class Meta:
        db_table = "tag"
        verbose_name = "task tag"
        verbose_name_plural = "task tags"
        default_related_name = "tags"

    name = models.SlugField(
        max_length=16,
        unique=True,
        verbose_name="tag name",
        help_text="Required. 16 characters or fewer"
    )

    # an alias to name field
    @property
    def tag(self):
        return self.name

    @tag.setter
    def tag(self, value):
        self.name = value

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"<Tag(pk={self.pk}, name='{self.name}')>"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.name


class TaskModel(models.Model):
    """Task model implementation

    :cvar id: unique task identifier, auto created by Django
    :type id: int
    :cvar created_at: time a task was created
    :type created_at: :class: `datetime.datetime`
    :cvar updated_at: time a task was last updated
    :type updated_at: :class: `datetime.datetime`
    :cvar title: task title, some descriptive summary
    :type title: str
    :cvar description: task detailed description
    :type description: str
    :cvar project: a project a task belongs to
    :type project: :class: `ProjectModel`
    :cvar tag: a tag related to a task
    :type tag: :class: `TaskTagModel`

    """

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = "updated_at", "project", "title"
        get_latest_by = "created_at"
        default_related_name = "tasks"

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False  # prevents this fields for being displayed on forms
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )
    title = models.CharField(
        max_length=128,
        verbose_name="task title",
        help_text="Required. 128 characters or fewer."
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="task detail description"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="tasks completed status"
    )

    # relationship
    project = models.ForeignKey(
        ProjectModel, on_delete=models.CASCADE,
        verbose_name="related project"
    )
    tag = models.ManyToManyField(
        TaskTagModel,
        verbose_name="related tags"
    )

    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True,
        verbose_name="reporter",
        related_name="reported_tasks"
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="assignee",
        related_name="assigned_tasks"
    )

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return f"<Task (pk={self.pk}, title='{self.title}')"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.title

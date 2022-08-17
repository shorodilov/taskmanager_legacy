import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name="ID"
                    )
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Required. 32 characters or fewer.",
                        max_length=32, verbose_name="project title"
                    )
                ),
                (
                    "summary",
                    models.CharField(
                        help_text="Required. 128 characters or fewer.",
                        max_length=128,
                        verbose_name="short project description"
                    )
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True,
                        verbose_name="detailed project description"
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskTagModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name="ID"
                    )
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required. 16 characters or fewer",
                        max_length=16, unique=True, verbose_name="tag name"
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name="ID"
                    )
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True)
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True)
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Required. 128 characters or fewer.",
                        max_length=128, verbose_name="task title"
                    )
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True,
                        verbose_name="task detail description"
                    )
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks", to="task.projectmodel",
                        verbose_name="related project"
                    )
                ),
                (
                    "tag",
                    models.ManyToManyField(
                        related_name="tasks", to="task.tasktagmodel",
                        verbose_name="related tags"
                    )
                ),
            ],
        ),
    ]

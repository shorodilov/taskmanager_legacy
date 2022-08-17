import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0002_task_complete_field"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projectmodel",
            options={
                "verbose_name": "project",
                "verbose_name_plural": "projects"
            },
        ),
        migrations.AlterModelOptions(
            name="taskmodel",
            options={
                "default_related_name": "tasks",
                "get_latest_by": "created_at",
                "ordering": ("updated_at", "project", "title"),
                "verbose_name": "task",
                "verbose_name_plural": "tasks"
            },
        ),
        migrations.AlterModelOptions(
            name="tasktagmodel",
            options={
                "default_related_name": "tags",
                "verbose_name": "task tag",
                "verbose_name_plural": "task tags"
            },
        ),
        migrations.AlterField(
            model_name="taskmodel",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="task.projectmodel",
                verbose_name="related project"
            ),
        ),
        migrations.AlterField(
            model_name="taskmodel",
            name="tag",
            field=models.ManyToManyField(
                to="task.tasktagmodel",
                verbose_name="related tags"
            ),
        ),
        migrations.AlterModelTable(
            name="projectmodel",
            table="project",
        ),
        migrations.AlterModelTable(
            name="taskmodel",
            table="task",
        ),
        migrations.AlterModelTable(
            name="tasktagmodel",
            table="tag",
        ),
    ]

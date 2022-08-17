import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user", "0001_initial"),
        ("task", "0004_tag_name_slugify"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskmodel",
            name="assignee",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=models.SET(0),
                related_name="assigned_tasks", to=settings.AUTH_USER_MODEL,
                verbose_name="assignee"
            ),
        ),
        migrations.AddField(
            model_name="taskmodel",
            name="reporter",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="reported_tasks", to=settings.AUTH_USER_MODEL,
                verbose_name="reporter"
            ),
        ),
    ]

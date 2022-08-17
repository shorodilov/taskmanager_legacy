from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskmodel",
            name="completed",
            field=models.BooleanField(
                default=False, verbose_name="tasks completed status"
            ),
        ),
    ]

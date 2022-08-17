from django.db import migrations, models
from django.utils.text import slugify


def migrate_forward(apps, schema_editor):
    """Slugify existing tags"""

    # noinspection PyPep8Naming
    TaskTagModel = apps.get_model("task", "TaskTagModel")
    db_alias = schema_editor.connection.alias
    qs = TaskTagModel.objects.using(db_alias).all()
    for obj in qs:
        obj.name = slugify(obj.name)
    TaskTagModel.objects.using(db_alias).bulk_update(qs, ["name"])


# noinspection PyUnusedLocal
def migrate_reverse(apps, schema_editor):
    pass  # no reverse migration


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0003_alter_tables_options"),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_reverse),
        migrations.AlterField(
            model_name="tasktagmodel",
            name="name",
            field=models.SlugField(
                help_text="Required. 16 characters or fewer", max_length=16,
                unique=True, verbose_name="tag name"
            ),
        ),
    ]

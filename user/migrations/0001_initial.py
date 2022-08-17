from django.contrib.auth import get_user_model
from django.db import migrations


# noinspection PyUnusedLocal
def create_default_user(app, schema_editor):
    # noinspection PyPep8Naming
    UserModel = get_user_model()
    db_alias = schema_editor.connection.alias
    UserModel.objects.using(db_alias).create(
        pk=0, username="unknown", is_active=False
    )


# noinspection PyUnusedLocal
def remove_default_user(app, schema_editor):
    # noinspection PyPep8Naming
    UserModel = get_user_model()
    db_alias = schema_editor.connection.alias
    UserModel.objects.using(db_alias).filter(pk=0).delete()


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_default_user, remove_default_user)
    ]

# Generated by Django 3.1.1 on 2020-11-06 00:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('international', '0003_loggedinuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoggedInUser',
            new_name='LoggedInUserInternational',
        ),
    ]

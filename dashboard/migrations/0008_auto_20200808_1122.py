# Generated by Django 3.0.8 on 2020-08-08 11:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_auto_20200808_1117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Profile',
        ),
    ]
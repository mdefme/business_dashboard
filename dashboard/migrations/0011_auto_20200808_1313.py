# Generated by Django 3.0.8 on 2020-08-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20200808_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='working_on',
            field=models.CharField(max_length=100),
        ),
    ]

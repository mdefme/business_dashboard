# Generated by Django 3.0.8 on 2020-08-01 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30, null=True)),
                ('project_description', models.CharField(max_length=200, null=True)),
                ('project_date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subproject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subproject_name', models.CharField(max_length=15, null=True)),
                ('subproject_n', models.IntegerField(null=True)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(max_length=30, null=True)),
                ('leader_approved_text', models.BooleanField(null=True)),
                ('leader_approved_image', models.BooleanField(null=True)),
                ('client_approved_text', models.BooleanField(null=True)),
                ('client_approved_image', models.BooleanField(null=True)),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Project')),
                ('subproject_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Subproject')),
            ],
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-21 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_todolist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='status',
        ),
    ]
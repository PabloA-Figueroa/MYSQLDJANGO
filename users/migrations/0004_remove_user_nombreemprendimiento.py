# Generated by Django 4.1.13 on 2024-01-11 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_nombreemprendimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nombreEmprendimiento',
        ),
    ]

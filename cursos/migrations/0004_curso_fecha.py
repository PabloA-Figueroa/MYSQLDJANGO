# Generated by Django 4.1.13 on 2023-12-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_curso_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
    ]
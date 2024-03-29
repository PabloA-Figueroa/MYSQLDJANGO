# Generated by Django 4.1.13 on 2024-01-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emprendimiento', '0002_emprendimiento_tipoemprendimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claseEmprendimiento', models.CharField(max_length=60)),
                ('tipoProducto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('emprendimiento', models.ManyToManyField(blank=True, to='emprendimiento.emprendimiento')),
            ],
        ),
    ]

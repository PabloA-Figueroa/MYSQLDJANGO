# Generated by Django 4.1.13 on 2024-01-14 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Cursos', '0002_imagen_recurso_texto_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoImagen',
            fields=[
                ('recurso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Cursos.recurso')),
                ('imagen', models.ImageField(upload_to='recursos/imagenes/')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Cursos.recurso',),
        ),
        migrations.CreateModel(
            name='RecursoTexto',
            fields=[
                ('recurso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Cursos.recurso')),
                ('texto', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Cursos.recurso',),
        ),
        migrations.CreateModel(
            name='RecursoVideo',
            fields=[
                ('recurso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Cursos.recurso')),
                ('video', models.FileField(upload_to='recursos/videos/')),
                ('url_video', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Cursos.recurso',),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
        migrations.DeleteModel(
            name='Texto',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AlterModelOptions(
            name='recurso',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RenameField(
            model_name='recurso',
            old_name='ContenidoCurso',
            new_name='contenido_curso',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='contenido_type',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='object_id',
        ),
        migrations.AddField(
            model_name='recurso',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
    ]

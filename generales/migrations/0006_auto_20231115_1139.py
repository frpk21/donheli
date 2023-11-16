# Generated by Django 3.2.19 on 2023-11-15 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0005_alter_reflexiones_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='fuente',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='subcategoria',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='ultima_hora',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='vistas',
        ),
        migrations.AddField(
            model_name='noticias',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='generales.categoria'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='orden_destacado',
            field=models.IntegerField(choices=[(0, 'Titulares'), (1, 'Destacado 1'), (2, 'Destacado 2'), (3, 'General')], default=0),
        ),
    ]

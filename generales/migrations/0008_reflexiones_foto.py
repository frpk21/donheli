# Generated by Django 3.2.19 on 2023-11-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0007_alter_noticias_imagen_destacado'),
    ]

    operations = [
        migrations.AddField(
            model_name='reflexiones',
            name='foto',
            field=models.FileField(default='', upload_to='imagenes/reflexiones/', verbose_name='Imagen Destacado (400 x 400 px)'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='nota',
            field=models.CharField(default='', max_length=150, verbose_name='Nota'),
        ),
    ]
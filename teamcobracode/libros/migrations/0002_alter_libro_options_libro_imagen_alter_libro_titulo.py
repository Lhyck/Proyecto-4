# Generated by Django 4.2.6 on 2023-11-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['-created'], 'verbose_name': 'libro', 'verbose_name_plural': 'libros'},
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(default='', upload_to='libros', verbose_name='imagen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=150, verbose_name='titulo'),
        ),
    ]
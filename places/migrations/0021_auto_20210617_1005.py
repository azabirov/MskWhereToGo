# Generated by Django 3.2 on 2021-06-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0020_alter_image_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='lat',
            field=models.FloatField(blank=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='lng',
            field=models.FloatField(blank=True, verbose_name='Долгота'),
        ),
    ]

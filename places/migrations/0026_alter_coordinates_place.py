# Generated by Django 3.2 on 2021-06-17 06:58

import annoying.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0025_auto_20210617_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='place',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место'),
        ),
    ]

# Generated by Django 3.2 on 2021-06-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_place_placeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='placeid',
            field=models.CharField(max_length=256, unique=True, verbose_name='ID места'),
        ),
    ]

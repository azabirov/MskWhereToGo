# Generated by Django 3.2 on 2021-06-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20210602_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='placeid',
            field=models.CharField(default=0, max_length=256, verbose_name='ID места'),
            preserve_default=False,
        ),
    ]

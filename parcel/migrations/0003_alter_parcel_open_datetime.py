# Generated by Django 4.2.14 on 2024-07-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0002_parcel_locker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='open_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date_published'),
        ),
    ]

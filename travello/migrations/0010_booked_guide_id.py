# Generated by Django 3.0.1 on 2020-01-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0009_trekkingguide_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='guide_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

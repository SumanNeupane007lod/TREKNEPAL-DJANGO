# Generated by Django 3.0.1 on 2020-01-13 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0013_auto_20200113_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='short_desc',
            new_name='long_desc',
        ),
    ]

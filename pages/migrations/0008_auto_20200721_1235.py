# Generated by Django 3.0.8 on 2020-07-21 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_favour_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='favour',
            new_name='Interest',
        ),
    ]

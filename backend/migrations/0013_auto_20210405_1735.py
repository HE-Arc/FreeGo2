# Generated by Django 3.1.7 on 2021-04-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_kmlfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kmlfile',
            old_name='kmlFile',
            new_name='kml_file',
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_fridge_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]

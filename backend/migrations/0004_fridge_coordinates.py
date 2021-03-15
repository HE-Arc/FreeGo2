# Generated by Django 3.1.7 on 2021-03-15 08:10

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210309_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridge',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0, 0), geography=True, srid=4326),
        ),
    ]
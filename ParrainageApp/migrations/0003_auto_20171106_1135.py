# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParrainageApp', '0002_auto_20171106_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filleuil',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ParrainageApp/static/ParrainageApp/img/'),
        ),
        migrations.AlterField(
            model_name='parrain',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ParrainageApp/static/ParrainageApp/img/'),
        ),
    ]

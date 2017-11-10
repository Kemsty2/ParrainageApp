# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filiaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Filleuil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noms', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(default=20)),
                ('photo', models.ImageField(null=True, upload_to='ParrainageApp/static/ParrainageApp/img/')),
                ('description', models.TextField()),
                ('Filiaire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ParrainageApp.Filiaire')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noms', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(default=20)),
                ('photo', models.ImageField(null=True, upload_to='ParrainageApp/static/ParrainageApp/img/')),
                ('description', models.TextField()),
                ('Filiaire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ParrainageApp.Filiaire')),
                ('filleuil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ParrainageApp.Filleuil')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DhtResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_hash', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=20)),
                ('data_hash', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=255)),
                ('extension', models.CharField(max_length=20)),
                ('classified', models.CharField(max_length=255)),
                ('source_ip', models.CharField(max_length=20)),
                ('tagged', models.CharField(max_length=255)),
                ('length', models.CharField(max_length=255)),
                ('create_time', models.CharField(max_length=255)),
                ('last_see', models.CharField(max_length=255)),
                ('requests', models.IntegerField(default=0, max_length=10)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('creator', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]

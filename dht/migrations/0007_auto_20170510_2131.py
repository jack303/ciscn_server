# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dht', '0006_auto_20170510_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchFilelist',
            fields=[
                ('info_hash', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('file_list', models.TextField()),
            ],
            options={
                'db_table': 'search_filelist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SearchHash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_hash', models.CharField(max_length=40, unique=True)),
                ('category', models.CharField(max_length=20)),
                ('data_hash', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=255)),
                ('extension', models.CharField(max_length=20)),
                ('classified', models.IntegerField()),
                ('source_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('tagged', models.IntegerField()),
                ('length', models.BigIntegerField()),
                ('create_time', models.DateTimeField()),
                ('last_seen', models.DateTimeField()),
                ('requests', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('creator', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'search_hash',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='resource_text',
            name='key_word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labeled_resource', to='dht.Keyword'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-01 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_id', models.TextField()),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]

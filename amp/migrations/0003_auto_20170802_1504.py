# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-02 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amp', '0002_playlist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='playlist_id',
            field=models.TextField(unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-23 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SvetlanaSite', '0010_auto_20180523_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='year',
        ),
    ]

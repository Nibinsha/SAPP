# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sappsapp', '0005_auto_20180124_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='univresults',
            name='semname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

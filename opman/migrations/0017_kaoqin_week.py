# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0016_auto_20160628_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaoqin',
            name='week',
            field=models.CharField(default=None, max_length=10, verbose_name='星期'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0014_auto_20160628_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='kaoqin',
            name='date',
            field=models.DateField(default=None, verbose_name='日期'),
        ),
    ]

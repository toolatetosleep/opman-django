# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0017_kaoqin_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kaoqin',
            name='late',
            field=models.FloatField(blank=True, null=True, verbose_name='迟到时间'),
        ),
        migrations.AlterField(
            model_name='kaoqin',
            name='plus',
            field=models.FloatField(blank=True, null=True, verbose_name='加班时间'),
        ),
    ]

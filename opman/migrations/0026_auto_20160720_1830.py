# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 10:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0025_gitsetting_sourcepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gittoken',
            name='id',
        ),
        migrations.AlterField(
            model_name='gittoken',
            name='fullname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='姓名'),
        ),
    ]

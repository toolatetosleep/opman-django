# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0023_gittoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gittoken',
            name='fullname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='姓名'),
        ),
    ]

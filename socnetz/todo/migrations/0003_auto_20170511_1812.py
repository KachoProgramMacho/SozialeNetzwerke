# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170511_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]

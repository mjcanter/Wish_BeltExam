# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishexam', '0003_auto_20170328_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='added_by',
            field=models.CharField(max_length=40),
        ),
    ]

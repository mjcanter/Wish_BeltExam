# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishexam', '0002_auto_20170328_0852'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prod',
            new_name='Items',
        ),
    ]

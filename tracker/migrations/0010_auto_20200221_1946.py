# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-02-21 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20200221_1540'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tracker_app',
            new_name='Tracker_incidents',
        ),
    ]

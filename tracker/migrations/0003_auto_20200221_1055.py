# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-02-21 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200221_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0006_auto_20170905_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visavariable',
            name='variable_type',
            field=models.SmallIntegerField(choices=[(0, 'configuration'), (1, 'acquisition'), (2, 'status')]),
        ),
    ]

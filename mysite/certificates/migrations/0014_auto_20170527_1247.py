# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0013_auto_20170527_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='college',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

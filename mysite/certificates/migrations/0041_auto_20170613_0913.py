# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0040_auto_20170613_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='template',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]

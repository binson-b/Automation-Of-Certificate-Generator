# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 07:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0013_auto_20170527_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisedevent',
            name='participant',
            field=models.ManyToManyField(null=True, related_name='user', through='certificates.UserCertificateInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='college',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

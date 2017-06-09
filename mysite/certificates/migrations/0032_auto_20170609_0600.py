# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0031_remove_usercertificateinfo_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usertype',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='event',
            field=models.CharField(default='here', max_length=100),
        ),
        migrations.AddField(
            model_name='usercertificateinfo',
            name='user_type',
            field=models.ManyToManyField(related_name='type_user', to='certificates.UserType'),
        ),
    ]

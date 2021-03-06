# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 06:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificates', '0006_auto_20170526_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCertificateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_attended', models.IntegerField()),
                ('qrCode', models.IntegerField()),
                ('organise_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.OrganiseProgram')),
                ('user', models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='organiseprogram',
            name='user1',
            field=models.ManyToManyField(related_name='user', through='certificates.UserCertificateInfo', to=settings.AUTH_USER_MODEL),
        ),
    ]

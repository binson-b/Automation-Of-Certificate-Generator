# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0042_auto_20170615_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.IntegerField(max_length=10)),
                ('dob', models.DateField()),
                ('college', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='organisedevent',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to='certificates.UserProfile'),
        ),
        migrations.AlterField(
            model_name='usercertificateinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.UserProfile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

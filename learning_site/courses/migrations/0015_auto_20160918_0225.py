# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20160917_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_live',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('i', 'In Progress'), ('r', 'In Review'), ('p', 'Published')], default='i', max_length=1),
        ),
    ]

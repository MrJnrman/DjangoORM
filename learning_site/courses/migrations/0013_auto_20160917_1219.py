# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_quiz_time_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='time_taken',
        ),
        migrations.AddField(
            model_name='quiz',
            name='time_takens',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]

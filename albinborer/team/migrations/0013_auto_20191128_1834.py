# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_auto_20191128_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='board_detail',
        ),
        migrations.AlterField(
            model_name='member',
            name='board_member',
            field=models.TextField(blank=True, max_length=220, null=True),
        ),
    ]

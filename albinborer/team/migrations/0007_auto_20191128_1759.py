# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-28 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20191126_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name=b'headshot',
            new_name='image',
        ),
    ]
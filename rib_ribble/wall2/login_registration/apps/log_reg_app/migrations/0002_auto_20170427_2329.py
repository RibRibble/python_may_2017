# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reg',
            new_name='User',
        ),
    ]

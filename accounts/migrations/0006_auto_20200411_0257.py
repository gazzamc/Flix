# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-11 02:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200411_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='subscribed_date',
            new_name='subscription_date',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='subscribed_end_date',
            new_name='subscription_end_date',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0009_auto_20170703_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='element_value',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
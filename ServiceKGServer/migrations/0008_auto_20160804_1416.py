# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceKGServer', '0007_advertisement_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='from_datetime',
            field=models.DateTimeField(null=True, verbose_name='FROM TIME'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='to_datetime',
            field=models.DateTimeField(null=True, verbose_name='TO TIME'),
        ),
    ]

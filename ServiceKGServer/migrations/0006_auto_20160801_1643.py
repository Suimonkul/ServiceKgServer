# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceKGServer', '0005_auto_20160731_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='phone_three',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d 3'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='phone_two',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d 2'),
        ),
    ]

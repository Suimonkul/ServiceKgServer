# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceKGServer', '0004_auto_20160903_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(unique=True, serialize=False, verbose_name='ID', primary_key=True),
        ),
    ]

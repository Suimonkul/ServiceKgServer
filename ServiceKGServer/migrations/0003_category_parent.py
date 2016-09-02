# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceKGServer', '0002_auto_20160901_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(verbose_name='parent', to='ServiceKGServer.Category', null=True),
        ),
    ]

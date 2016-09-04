# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceKGServer', '0003_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='order',
            field=models.IntegerField(default=1, help_text='\u0432 \u0441\u043e\u043c\u0430\u0445', verbose_name='\u0426\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0438'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(verbose_name='parent', blank=True, to='ServiceKGServer.Category', null=True),
        ),
    ]

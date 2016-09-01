# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceKGServer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='active',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='title',
            field=models.CharField(default=1, max_length=120, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.CharField(max_length=120, verbose_name='\u0418\u043c\u044f'),
        ),
    ]

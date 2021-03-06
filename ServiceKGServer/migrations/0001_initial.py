# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name='\u0418\u043c\u044f')),
                ('description', models.CharField(max_length=10000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('phone', models.IntegerField(verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('phone_two', models.IntegerField(null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d 2', blank=True)),
                ('phone_three', models.IntegerField(null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d 3', blank=True)),
                ('order', models.CharField(max_length=100, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0438', blank=True)),
                ('position', models.IntegerField(verbose_name='\u041f\u043e\u0437\u0438\u0446\u0438\u044f')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e', to='ServiceKGServer.Category', null=True),
        ),
    ]

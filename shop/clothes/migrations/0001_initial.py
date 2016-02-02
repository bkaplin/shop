# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=12, choices=[(b'B', b'Black'), (b'D', b'Dark blue')])),
                ('size', models.IntegerField(choices=[(b'48', b'48'), (b'50', b'50'), (b'52', b'52'), (b'54', b'54'), (b'56', b'56'), (b'58', b'58')])),
                ('short_description', models.CharField(help_text='\u043a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', max_length=255, null=True, blank=True)),
                ('description', models.TextField(help_text='\u043f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='size',
            field=models.CharField(max_length=3, choices=[(b'48', b'48'), (b'50', b'50'), (b'52', b'52'), (b'54', b'54'), (b'56', b'56'), (b'58', b'58')]),
            preserve_default=True,
        ),
    ]

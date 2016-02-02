# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20160202_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='image_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

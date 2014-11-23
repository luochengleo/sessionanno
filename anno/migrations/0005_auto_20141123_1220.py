# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0004_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='action',
            field=models.CharField(default='NONE', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log',
            name='query',
            field=models.CharField(default='NONE', max_length=100),
            preserve_default=False,
        ),
    ]

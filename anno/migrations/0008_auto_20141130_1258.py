# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0007_auto_20141130_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='question',
            field=models.CharField(default='???', max_length=1000),
            preserve_default=False,
        ),
    ]

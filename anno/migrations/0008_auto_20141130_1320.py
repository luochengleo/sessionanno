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
            model_name='query',
            name='stopCrawl',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='query',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]

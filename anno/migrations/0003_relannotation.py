# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0002_recordannotation_recordfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelAnnotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annotatorID', models.CharField(max_length=50)),
                ('task_id', models.IntegerField()),
                ('query', models.CharField(max_length=100)),
                ('result_id', models.CharField(max_length=50)),
                ('result_url', models.CharField(max_length=1024)),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

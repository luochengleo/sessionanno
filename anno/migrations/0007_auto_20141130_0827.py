# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0006_auto_20141129_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionAnnotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentID', models.CharField(max_length=50)),
                ('task_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='query',
            name='lastcrawledpage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='query',
            name='recomm',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='query',
            name='resultnum',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]

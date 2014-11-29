# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0005_auto_20141123_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studentID', models.CharField(max_length=50)),
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
        migrations.AddField(
            model_name='searchresult',
            name='result_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

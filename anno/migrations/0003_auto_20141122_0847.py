# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anno', '0002_auto_20141117_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillingQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('task', models.ManyToManyField(to='anno.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SingleChoiceQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('choices', models.CharField(max_length=5000)),
                ('answer', models.IntegerField()),
                ('task', models.ManyToManyField(to='anno.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='init_query',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]

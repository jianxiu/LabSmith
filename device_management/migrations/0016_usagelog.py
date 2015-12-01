# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0015_remove_maintainlog_countnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsageLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('machineName', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=20, null=True, blank=True)),
                ('reserveTimestamp', models.DateTimeField()),
                ('releaseTimestamp', models.DateTimeField()),
                ('isUse', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

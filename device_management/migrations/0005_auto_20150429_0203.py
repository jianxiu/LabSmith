# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0004_auto_20150429_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='user',
        ),
        migrations.AddField(
            model_name='device',
            name='cuser',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0012_auto_20150605_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='pxeFilePath',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]

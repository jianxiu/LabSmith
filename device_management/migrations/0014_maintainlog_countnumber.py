# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0013_device_pxefilepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintainlog',
            name='countNumber',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]

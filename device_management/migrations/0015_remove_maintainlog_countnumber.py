# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0014_maintainlog_countnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintainlog',
            name='countNumber',
        ),
    ]

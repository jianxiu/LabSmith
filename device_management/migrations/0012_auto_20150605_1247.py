# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0011_auto_20150603_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintainlog',
            old_name='name',
            new_name='MachineName',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device_management', '0009_device_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintainLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=1000, null=True, blank=True)),
                ('name', models.ForeignKey(to='device_management.Device')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='device',
            name='content',
        ),
    ]

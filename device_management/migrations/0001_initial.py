# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('info', models.CharField(max_length=1000, null=True, blank=True)),
                ('spa_ip', models.CharField(max_length=20)),
                ('spb_ip', models.CharField(max_length=20)),
                ('spa_mac', models.CharField(max_length=17, null=True, blank=True)),
                ('spb_mac', models.CharField(max_length=17, null=True, blank=True)),
                ('mgmt_ip', models.CharField(max_length=20)),
                ('spa_term', models.CharField(max_length=30)),
                ('spb_term', models.CharField(max_length=30)),
                ('owner', models.ForeignKey(related_name='owner_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('wanted', models.ForeignKey(related_name='wanted_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('msg', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('device', models.ForeignKey(to='device_management.Device')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        # migrations.CreateModel(
        #     name='MaintainLog',
        #     fields=[
        #         ('id', models.AutoField(serialize=False, primary_key=True)),
        #         ('MachineName', models.CharField(max_length=30)),
        #         ('user', models.CharField(max_length=20,blank=True,null=True)),
        #         ('timestamp', models.DateTimeField()),
        #         ('content', models.CharField(max_length=1000,blank=True,null=True)),
        #     ],
        #     options={
        #     },
        #     bases=(models.Model,),
        # ),
    ]

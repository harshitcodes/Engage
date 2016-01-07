# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(related_name='follower', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

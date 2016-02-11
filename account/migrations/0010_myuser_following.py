# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20160115_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]

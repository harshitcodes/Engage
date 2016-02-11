# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20160115_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='of_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_project'),
        ),
    ]

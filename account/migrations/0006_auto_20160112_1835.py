# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20160111_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mentor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='user_projects', default=1),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_links',
            field=models.TextField(help_text='Prefer Linked In Profile', default='--', validators=[django.core.validators.URLValidator()]),
        ),
    ]

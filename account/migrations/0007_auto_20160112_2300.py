# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20160112_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='year',
            field=models.CharField(choices=[('1st', 'First Year'), ('2nd', 'Second Year'), ('3rd', 'Third Year'), ('4th', 'Fourth')], default='--', max_length=3),
        ),
        migrations.AddField(
            model_name='project',
            name='is_team',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='team_member',
            field=models.ManyToManyField(related_name='member_of_team', to=settings.AUTH_USER_MODEL),
        ),
    ]

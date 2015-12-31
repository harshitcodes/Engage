# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_skill_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='contact',
        ),
    ]

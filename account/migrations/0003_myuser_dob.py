# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160106_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]

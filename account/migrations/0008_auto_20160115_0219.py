# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20160112_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='related_link',
            field=models.CharField(max_length=254, unique=True, blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]

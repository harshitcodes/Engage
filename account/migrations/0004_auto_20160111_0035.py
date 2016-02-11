# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_myuser_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('related_link', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_links',
            field=models.TextField(default='--', validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='project',
            name='of_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('text', models.CharField(max_length=160)),
                ('image', models.ImageField(null=True, upload_to='media/feed_pics', blank=True)),
                ('link', models.TextField(null=True, blank=True)),
                ('upload_file', models.FileField(null=True, upload_to='files/', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=30)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(blank=True, upload_to='media/profile_pics')),
                ('gender', models.CharField(default='NS', choices=[('NS', '--'), ('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('roll_no', models.BigIntegerField(default=0, verbose_name='Roll Number', blank=True)),
                ('branch', models.CharField(default='NS', verbose_name='Branch', choices=[('NS', '--'), ('CSE', 'Computer Science Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electronics and Electrical Engineering'), ('ICE', 'Instrumentation and Control Engineering')], blank=True, max_length=3, null=True)),
                ('groups', models.ManyToManyField(related_query_name='user', to='auth.Group', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', to='auth.Permission', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('tags', models.CharField(max_length=30)),
                ('saved', models.BooleanField(default=False)),
                ('of_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='user_skills')),
            ],
        ),
    ]

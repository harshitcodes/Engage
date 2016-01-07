# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, error_messages={'unique': 'A user with that username already exists.'}, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/', blank=True)),
                ('gender', models.CharField(max_length=1, default='M', choices=[('M', 'Male'), ('F', 'Female')])),
                ('dob', models.DateField(null=True, blank=True)),
                ('following', models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True)),
            ],
            options={
                'verbose_name': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('Profile_Pic', models.ImageField(upload_to='User_ProfilePics/', blank=True)),
                ('skill_set', models.CharField(max_length=20, default=('', 'Null'), choices=[('', 'Null'), ('C', 'C'), ('C++', 'C++'), ('Python', 'Python'), ('JAVA', 'JAVA'), ('Javascript', 'Javascript'), ('Web Development', 'Web Development'), ('Django', 'Django'), ('Ruby On Rails', 'Ruby On Rails'), ('Android App Development', 'Android App Development'), ('iOS App Development', 'iOS App Development'), ('Microprocessors', 'Microprocessors'), ('C#', 'C#'), ('Electronics', 'Electronics'), ('HTML', 'HTML'), ('HTML 5', 'HTML 5'), ('CSS', 'CSS'), ('CSS3', 'CSS3'), ('jQuery', 'jQuery'), ('Data Structures', 'Data Structures'), ('Algorithms', 'Algorithms'), ('Robotics', 'Robotics'), ('Bootstrap', 'Bootstrap'), ('Perl', 'Perl'), ('.NET', '.NET'), ('Data Mining', 'Data Mining'), ('Big Data', 'Big Data'), ('Cloud Computing', 'Cloud Computing'), ('UX Design', 'UX Design'), ('Photoshop', 'Photoshop'), ('SQL', 'SQL'), ('GNU/Linux', 'GNU/Linux'), ('Embedded System', 'Embedded System'), ('VLSI', 'VLSI')])),
                ('followers', models.ManyToManyField(related_name='following_me', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='myuser',
            unique_together=set([('email',)]),
        ),
    ]

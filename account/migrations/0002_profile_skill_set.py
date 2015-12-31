# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skill_set',
            field=models.CharField(choices=[('', 'Null'), ('C', 'C'), ('C++', 'C++'), ('Python', 'Python'), ('JAVA', 'JAVA'), ('Javascript', 'Javascript'), ('Web Development', 'Web Development'), ('Django', 'Django'), ('Ruby On Rails', 'Ruby On Rails'), ('Android App Development', 'Android App Development'), ('iOS App Development', 'iOS App Development'), ('Microprocessors', 'Microprocessors'), ('C#', 'C#'), ('Electronics', 'Electronics'), ('HTML', 'HTML'), ('HTML 5', 'HTML 5'), ('CSS', 'CSS'), ('CSS3', 'CSS3'), ('jQuery', 'jQuery'), ('Data Structures', 'Data Structures'), ('Algorithms', 'Algorithms'), ('Robotics', 'Robotics'), ('Bootstrap', 'Bootstrap'), ('Perl', 'Perl'), ('.NET', '.NET'), ('Data Mining', 'Data Mining'), ('Big Data', 'Big Data'), ('Cloud Computing', 'Cloud Computing'), ('UX Design', 'UX Design'), ('Photoshop', 'Photoshop'), ('SQL', 'SQL'), ('GNU/Linux', 'GNU/Linux'), ('Embedded System', 'Embedded System'), ('VLSI', 'VLSI')], max_length=20, default=('', 'Null')),
        ),
    ]

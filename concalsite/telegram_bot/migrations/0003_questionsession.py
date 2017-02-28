# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20170227_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSession',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_session', models.IntegerField()),
                ('user_answer', models.CharField(max_length=10)),
                ('confidence', models.IntegerField()),
                ('id_question', models.ForeignKey(to='questions.State')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

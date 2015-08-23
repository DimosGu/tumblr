# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='blog',
        ),
        migrations.AddField(
            model_name='site',
            name='domain',
            field=models.CharField(max_length=255, default=None),
        ),
    ]

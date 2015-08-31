# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20150821_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub date'),
        ),
    ]

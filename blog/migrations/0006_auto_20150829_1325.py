# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150828_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name='pub date', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='follow',
            name='pub_date',
            field=models.DateTimeField(verbose_name='pub date', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='pub date', default=django.utils.timezone.now),
        ),
    ]

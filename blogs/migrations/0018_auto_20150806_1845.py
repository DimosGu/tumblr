# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_auto_20150806_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]

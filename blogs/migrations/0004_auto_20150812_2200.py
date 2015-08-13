# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20150812_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=blogs.models.upload_path, blank=True),
        ),
    ]

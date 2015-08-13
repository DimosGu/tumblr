# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20150809_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='user_media/%Y/%m/%d'),
        ),
    ]

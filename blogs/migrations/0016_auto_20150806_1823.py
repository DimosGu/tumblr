# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20150806_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file_field',
            new_name='file',
        ),
    ]

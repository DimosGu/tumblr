# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20150806_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file',
            new_name='file_field',
        ),
    ]

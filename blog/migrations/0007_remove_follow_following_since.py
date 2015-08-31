# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150829_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='following_since',
        ),
    ]

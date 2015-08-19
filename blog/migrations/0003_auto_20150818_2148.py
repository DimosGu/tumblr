# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_follow_following_since'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follow',
            new_name='blog',
        ),
    ]

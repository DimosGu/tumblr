# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AddField(
            model_name='post',
            name='some_file',
            field=models.FileField(null=True, blank=True, upload_to='/media/'),
        ),
    ]

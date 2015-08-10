# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blogs.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to=blogs.models.upload_path, default='/media/default_blog_img.png'),
        ),
    ]

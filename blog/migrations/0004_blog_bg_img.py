# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150818_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bg_img',
            field=models.ImageField(default='/media/default_blog_bg.png', upload_to=blog.models.upload_path),
        ),
    ]

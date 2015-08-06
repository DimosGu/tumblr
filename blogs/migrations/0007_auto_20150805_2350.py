# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20150805_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='/tumblr/media/default_blog_img.png', upload_to='media'),
        ),
    ]

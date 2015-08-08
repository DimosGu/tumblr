# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_auto_20150806_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='/media/post', default='/media/default_blog_img.png'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='/media/post'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0022_auto_20150806_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='media', default='/media/default_blog_img.png'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to='media', blank=True),
        ),
    ]

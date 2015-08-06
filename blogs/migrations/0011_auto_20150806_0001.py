# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20150806_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='/media/default_blog_img.png', upload_to='/media/'),
        ),
    ]

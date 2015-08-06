# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20150804_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='media', default='media/default_blog_img.png'),
        ),
    ]

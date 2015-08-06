# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20150805_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='media', default='MEDIA_URLdefault_blog_img.png'),
        ),
    ]

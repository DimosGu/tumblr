# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_bg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub_date'),
        ),
        migrations.AddField(
            model_name='follow',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub_date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='pub_date'),
        ),
    ]

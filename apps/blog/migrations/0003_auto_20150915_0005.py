# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='blog',
            field=models.ForeignKey(to='blog.Blog', unique=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(to='blog.Post', unique=True),
        ),
    ]

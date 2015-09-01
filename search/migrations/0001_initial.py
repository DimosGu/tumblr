# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pub_date', models.DateTimeField(verbose_name='pub date', default=django.utils.timezone.now)),
                ('tags', models.CharField(max_length=20, blank=True)),
                ('post', models.ManyToManyField(to='blog.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

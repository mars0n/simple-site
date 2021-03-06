# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-10 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplesite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='seo_description',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='SEO Meta Description'),
        ),
        migrations.AddField(
            model_name='page',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='SEO Meta Keywords'),
        ),
        migrations.AddField(
            model_name='page',
            name='seo_title',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='SEO Title'),
        ),
    ]

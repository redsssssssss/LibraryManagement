# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
                name='Book',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('name', models.CharField(max_length=128)),
                    ('price', models.FloatField()),
                    ('author', models.CharField(max_length=128)),
                    ('pubDate', models.DateField()),
                    ('typ', models.CharField(max_length=128)),
                ],
        ),
        migrations.CreateModel(
                name='Img',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('name', models.CharField(max_length=128)),
                    ('desc', models.TextField()),
                    ('img', models.ImageField(upload_to='./image/%Y/%m/%d/')),
                    ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Book')),
                ],
        ),
        migrations.CreateModel(
                name='MyUser',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('nickname', models.CharField(max_length=16)),
                    ('permission', models.IntegerField()),
                    ('user',
                     models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-18 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20)),
                ('b_age', models.IntegerField(default=18)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=20)),
                ('g_price', models.IntegerField(default=100)),
                ('g_buyer', models.ManyToManyField(to='two.Buyer')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-18 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180718_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_name', models.CharField(max_length=20)),
                ('h_price', models.IntegerField(default=100)),
                ('h_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Person')),
            ],
        ),
        migrations.AlterField(
            model_name='idcard',
            name='id_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Person'),
        ),
    ]

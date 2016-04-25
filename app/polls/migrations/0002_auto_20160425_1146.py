# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('remarks', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Mouth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mouth', models.IntegerField()),
                ('initial', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Person')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='mouth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Mouth'),
        ),
    ]
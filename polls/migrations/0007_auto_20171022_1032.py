# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170722_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'keuze', 'verbose_name_plural': 'keuzes'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'stemming', 'verbose_name_plural': 'stemmingen'},
        ),
        migrations.AddField(
            model_name='question',
            name='question_advice',
            field=models.CharField(choices=[('positive', 'Overnemen'), ('neutral', 'Neutraal'), ('negative', 'Niet overnemen')], default='neutral', max_length=4000, verbose_name='Advies Programmacommissie'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_category',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=2, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_change',
            field=models.CharField(default='', max_length=4000, verbose_name='Wijziging'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_people',
            field=models.CharField(default='', max_length=4000, verbose_name='Indieners'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=2000, verbose_name='Titel'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0068_auto_20160815_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonPrize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('rank', models.PositiveIntegerField()),
                ('max_rating', models.PositiveIntegerField(blank=True, null=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Season')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonPrizeWinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
                ('season_prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.SeasonPrize')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='seasonprizewinner',
            unique_together=set([('season_prize', 'player')]),
        ),
        migrations.AlterUniqueTogether(
            name='seasonprize',
            unique_together=set([('season', 'rank', 'max_rating')]),
        ),
    ]

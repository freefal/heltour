# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0057_auto_20160812_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='LonePlayerPairing2',
            fields=[
                ('playerpairing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tournament.PlayerPairing')),
                ('pairing_order', models.PositiveIntegerField()),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round')),
            ],
            options={
                'abstract': False,
            },
            bases=('tournament.playerpairing',),
        ),
        migrations.CreateModel(
            name='TeamPlayerPairing2',
            fields=[
                ('playerpairing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tournament.PlayerPairing')),
                ('board_number', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('team_pairing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.TeamPairing')),
            ],
            bases=('tournament.playerpairing',),
        ),
        migrations.AlterUniqueTogether(
            name='teamplayerpairing2',
            unique_together=set([('team_pairing', 'board_number')]),
        ),
        migrations.RunSQL('''
        INSERT INTO tournament_teamplayerpairing2 ( team_pairing_id, playerpairing_ptr_id, board_number )
                             SELECT team_pairing_id, player_pairing_id, board_number FROM tournament_teamplayerpairing;
         INSERT INTO tournament_loneplayerpairing2 ( round_id, playerpairing_ptr_id, pairing_order )
                             SELECT round_id, player_pairing_id, pairing_order FROM tournament_loneplayerpairing;
        ''')
    ]

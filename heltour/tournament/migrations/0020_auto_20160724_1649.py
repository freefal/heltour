# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0019_auto_20160724_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='agreed_to_rules',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='already_in_slack_group',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='can_commit',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='registration',
            name='has_played_20_games',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]

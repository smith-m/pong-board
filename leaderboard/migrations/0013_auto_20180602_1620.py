# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0012_ranking_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranking',
            old_name='score',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='ranking',
            name='id',
        ),
        migrations.AlterField(
            model_name='ranking',
            name='player',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='leaderboard.Player'),
        ),
    ]
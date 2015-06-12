# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from dotaPredictor.services.match_history_service import *
from dotaPredictor.csvrepo.hero_repo import *


def import_heroes(apps, schema_editor):
    hr = HeroRepository()
    heroes = hr.get_dota_heros_from_json(None)
    print len(heroes)
    for hero in heroes:
        hero.save()


def import_matches():
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('dotaPredictor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_heroes),
    ]

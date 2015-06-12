import json
import os
import dotaPredictor.cfg.configuration as cfg
from dotaPredictor.datamodels.hero import *


class HeroRepository:
    # class variables
    JSON_HERO_FILE = os.path.abspath(''.join([os.getcwd(), os.path.normpath("../../dota2-api/data/heroes.json")]))

    def __init__(self):
        self.dota_heroes = []
        # cache heroes by all three types for quick lookups
        self.dota_heroes_by_id = None
        self.dota_heroes_by_local_name = None
        self.dota_heroes_by_name = None
        if(cfg.repo_cfg.get("RepositorySettings", "use_database") is False):
            self.get_dota_heros_from_json(None)

    def get_dota_heros_from_json(self, file_name):
        if file_name is None:
            file_name = self.JSON_HERO_FILE

        # if the hero list has not already been been populated
        if len(self.dota_heroes) == 0:
            with open(file_name) as f:
                heroes_json = json.load(f)
            for jsonhero in heroes_json.get("heroes"):
                hero = Hero(hero_id=jsonhero['id'], name=jsonhero['name'], local_name=jsonhero['localized_name'])
                self.dota_heroes.append(hero)
                # self.dota_heroes_by_id[hero.]
        return self.dota_heroes

    def get_dota_hero_by_name(self, name):
        pass

    def get_dota_hero_by_id(self, id):
        pass

    def get_dota_hero_by_local_name(self, name):
        pass

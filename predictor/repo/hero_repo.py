import json


class HeroRepository:
    JSON_HERO_FILE = os.path.abspath(''.join([os.getcwd(), os.path.normpath("../../dota2-api/data/heroes.json")]))

    def __init__(self):
        self.dota_heroes = None

    def get_dota_heros_from_json(file):
        if self.dota_heroes is None:
        	
        return self.dota_heroes

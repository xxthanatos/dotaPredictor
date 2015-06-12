from django.test import TestCase

# Create your tests here.
from dotaPredictor.services.match_history_service import *
from dotaPredictor.datamodels.hero import *


class ImportCsvMatchesTestCase(TestCase):

    def setUp(self):
        self.mhs = MatchService()
        self.hr = HeroRepository()

    def test_match_import(self):
        '''matches = self.mhs.get_local_name_csv_matches(None)
        for match in matches:
            #print ("matches " + match.__str__())
            pass'''

    def test_hero_import(self):
        heroes = self.hr.get_dota_heros_from_json(None)
        print len(heroes)
        for hero in heroes:
            hero.save()

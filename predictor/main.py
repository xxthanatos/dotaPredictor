from repo.match_repo import *
from repo.hero_repo import *


hr = HeroRepository()
heroes = hr.get_dota_heros_from_json(hr.JSON_HERO_FILE)
print heroes

mh = MatchRepository()
print mh.get_csv_match_history(mh.TEST_CSV_FILE_PATH, heroes)

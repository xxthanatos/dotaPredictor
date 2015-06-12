from dotaPredictor.csvrepo.hero_repo import HeroRepository
from dotaPredictor.csvrepo.match_repo import MatchRepository


class MatchService:

    def __init__(self):
        self.match_repo = MatchRepository()
        self.hero_repo = HeroRepository()

    def get_local_name_csv_matches(self, file_name):
        """ return a list of matches with hero objects filled in. The given csv file uses local_name to define the heroes"""

        matches = self.match_repo.parse_csv_match_history(file_name)
        for match in matches:
            for hero in match[0:9]:
                print hero
        return matches

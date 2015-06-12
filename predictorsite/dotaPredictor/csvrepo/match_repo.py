import sys
import os
from dotaPredictor.datamodels.match import *


class MatchRepository:
    TEST_CSV_FILE_PATH = os.path.abspath(''.join([os.getcwd(), os.path.normpath("../../docs/dotaMatchHistory.csv")]))

    def __init__(self):
        self.current_id = 0

    def parse_csv_match_history(self, file_name):
        """" return an array of matches in a csv file written in the following format:
        hero1,hero2,hero3,hero4,hero5,hero1,hero2,hero3,hero4,hero5,winner

        The returned array will be a list of match objects of the format:
        t1 = [hero1,hero2,hero3,hero4,hero5]
        t2 = [hero1,hero2,hero3,hero4,hero5]
        winner = winner     (1,2) to select the winning team
        """

        matches = []
        if file_name is None:
            file_name = self.TEST_CSV_FILE_PATH
            print(file_name)

        with open(file_name) as f:
            for line in f:
                matches.append(self.parse_csv_line(line))
        return matches

    def parse_csv_line(self, line):
        match_split = line.split(",")
        team1 = match_split[0:5]
        team2 = match_split[5:10]
        winner = match_split[10]
        self.current_id += 1
        return Match(self.current_id, team1, team2, winner)

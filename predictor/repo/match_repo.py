import sys
import os
from data import *
import hero_repo


class MatchRepository:
    TEST_CSV_FILE_PATH = os.path.abspath(''.join([os.getcwd(), os.path.normpath("../../docs/dotaMatchHistory.txt")]))

    def __init__(self):
        pass

    def get_csv_match_history(self, file, heroes):
        matches = []
        with open(file) as f:
            for line in f:
                matches.append(self.parse_csv_line(line))
        print matches

    def parse_csv_line(self, line):
        print line
        return line

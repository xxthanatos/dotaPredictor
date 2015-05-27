class Match:

    def __init__(self, id, t1, t2, winner):
        # dire
        self.set_team1(t1)
        # radiant
        self.set_team2(t2)
        self.winner = winner

    def set_team1(self, t1):
        if(len(t1) != 5):
            raise IndexError(''.join(["Team1 size:", str(len(t1)), " Team sizes must be equal to 5"]))
        self.t1 = t1

    def set_team2(self, t2):
        if(len(t2) != 5):
            raise IndexError(''.join(["Team2 size:", str(len(t2)), " Team sizes must be equal to 5"]))
        self.t1 = t2


if __name__ == '__main__':
    test = Match(None, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1)
    bad = Match(None, [1, 3, 4, 5], [1, 2, 3, 5], 1)

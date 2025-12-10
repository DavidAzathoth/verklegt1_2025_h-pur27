class Match:
    def __init__(self, matchID: str, team_A: str, team_B: str, matchWinner: str = None, Score: dict = {} ,matchPlayed: bool = False):
        self.matchID = matchID
        self.team_A = team_A
        self.team_B = team_B
        self.matchWinner = matchWinner
        self.Score = Score
        self.matchPlayed = matchPlayed
    def createCSVDict(self):
        ret_dic={'matchID':self.matchID,'team_A':self.team_A,'team_B':self.team_B,'matchWinner':self.matchWinner,'playerScore':self.Score,'matchPlayed':self.matchPlayed}
        return ret_dic
    def __str__(self):
        ret_str = f'- Match {self.matchID:<{4}}: {self.team_A:>{14}} vs {self.team_B:<{14}} Date: fucking never'
        return ret_str

class Match:
    def __init__(self, matchID: str, team_A: str, team_B: str, matchWinner: str = None, Score: dict = {} ,matchPlayed: bool = False, matchDate: str = None, matchTime: str = None, server: int = None):
        self.matchID = matchID
        self.team_A = team_A
        self.team_B = team_B
        self.matchWinner = matchWinner
        self.Score = Score
        self.matchPlayed = matchPlayed
        self.matchDate = matchDate
        self.matchTime = matchTime
        self.server = server
    def createCSVDict(self):
        ret_dic={
            'matchID': self.matchID,
            'team_A': self.team_A,
            'team_B': self.team_B,
            'matchWinner': self.matchWinner,
            'playerScore': self.Score,
            'matchPlayed': self.matchPlayed,
            'matchDate': self.matchDate,
            'matchTime': self.matchTime,
            'server': self.server
            }
        return ret_dic
    def __str__(self): 
        ret_str=f"""


"""
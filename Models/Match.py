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
        """Creates a dictionary to store in a csv file"""
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
        """Used to print for updating matches by organizer"""
        ret_str = f"""
Match {self.matchID}: {self.team_A} vs {self.team_B}
"""
        return ret_str





    def returninfo(self):
        """Returns info for match, returns TBD or Not decided for match winner and score when match has not been played"""
        ret_str = f"""
Match {self.matchID}
Team 1: {self.team_A}
vs
Team 2: {self.team_B}

Match winner: {self.matchWinner if self.matchWinner in [self.team_A,self.team_B] else 'Not decided'}

Score: 
{self.team_A}: {self.Score.get(self.team_A) if len(self.Score)>1 else 'TBD'}
{self.team_B}: {self.Score.get(self.team_B) if len(self.Score)>1 else 'TBD'}
"""
        return ret_str
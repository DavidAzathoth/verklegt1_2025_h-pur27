class Match:
    def __init__(self, matchID: str, team_A: str, team_B: str, matchWinner: str = None, playerScore: dict = {} ,matchPlayed: bool = False):
        self.matchID = matchID
        self.team_A = team_A
        self.team_B = team_B
        self.matchWinner = matchWinner
        self.playerScore = playerScore
        self.matchPlayed = matchPlayed
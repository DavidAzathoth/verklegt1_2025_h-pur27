class Team:
    """Creates a team object
## Attributes for Team:
      \nteamID 
      \nteamName 
      \nroster
      \nwins
      \nlosses"""
    def __init__(self, teamID: str, teamName: str, roster: list, wins: int, losses: int, captainHandle: str):
        self.teamID: str = teamID
        self.teamName: str = teamName
        self.roster: list = roster.split(',')
        self.wins: int = wins
        self.losses: int = losses
        self.captainHandle: str = captainHandle

    def createCSVString(self):
        """Creates a row to store in a csv file"""
        ret_string=f'{self.teamID},{self.teamName},"{",".join(self.roster)}",{self.wins},{self.losses},{self.captainHandle}'
        return ret_string
    
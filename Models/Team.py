class Team:
    """Creates a team object
## Attributes for Team:
      \nteamID 
      \nteamName 
      \nroster
      \nwins
      \nlosses"""
    def __init__(self, teamID: str, teamName: str, roster: str, wins: int, losses: int, captainHandle: str, playerinstances:list = []):
        self.teamID: str = teamID
        self.teamName: str = teamName
        self.roster: list = roster.split(',')
        self.wins: int = wins
        self.losses: int = losses
        self.captainHandle: str = captainHandle
        self.playerinstances = playerinstances

    def createCSVString(self):
        """Creates a CSV file string"""
        ret_string=f'{self.teamID},{self.teamName},"{",".join(self.roster)}",{self.wins},{self.losses},{self.captainHandle}'
        return ret_string
    def createCSVDict(self)-> dict:
        """Creates a dictionary to store in a csv file"""
        ret_dic={'teamID':self.teamID,'teamName':self.teamName,'roster':(",".join(self.roster)),'wins':self.wins,'losses':self.losses,'captainHandle':self.captainHandle}
        return ret_dic
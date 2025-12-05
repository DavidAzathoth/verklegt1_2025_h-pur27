class Team:
    """Creates a team object
## Attributes for Team:
      \nteamID 
      \nteamName 
      \nroster
      \nwins
      \nlosses"""
    def __init__(self, teamID: str, teamName: str, roster: str = '', wins: int = 0, losses: int = 0, captainHandle: str = None, playerinstances:list = []):
        self.teamID: str = teamID
        self.teamName: str = teamName
        self.roster: list = roster.split(',')
        self.wins: int = int(wins)
        self.losses: int = int(losses)
        self.captainHandle: str = captainHandle
        self.playerinstances = playerinstances

    def createCSVString(self):
        """Creates a CSV file string"""
        ret_string=f'{self.teamID},{self.teamName},"{",".join(self.roster)}",{self.wins},{self.losses},{self.captainHandle}'
        return ret_string
    def createCSVDict(self)-> dict:
        """Creates a dictionary to store in a csv file"""
        ret_dic={'teamID':self.teamID,'teamName':self.teamName,'roster':(",".join(self.roster)),'wins':str(self.wins),'losses':str(self.losses),'captainHandle':self.captainHandle}
        return ret_dic
#    def __str__(self):
#        players = '\n'
#        return f"""
#Team name: {self.teamName}
#Players
#Address: {self.address}
#Phone number: {self.phoneNumber}
#E-mail: {self.emailAddress}
#Link: {self.link}
#        """

#---------------------------
#RU's e-Sport Extravaganza
#---------------------------
#View Team
#Team name: Team 1
#Players:
#1. Sheriff_Norris
#2. Player_A
#3. Player_B
#4. Player_C
#5. Player_D
#0. Back
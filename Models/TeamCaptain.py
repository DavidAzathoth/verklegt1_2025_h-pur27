class TeamCaptain:
    def __init__(self,captainHandle: str, player: object, hasTeam: bool = False):
        self.player = player
        self.captainHandle = captainHandle
        self.hasTeam = hasTeam
    def createCSVString(self):
        ret_string=(self.player).createCSVString()
        return ret_string

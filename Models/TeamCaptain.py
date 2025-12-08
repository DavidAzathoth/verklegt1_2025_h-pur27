class TeamCaptain:
    def __init__(self,captainHandle: str, player: object, hasTeam: bool = False, captaininstances = []):
        self.player = player
        self.captainHandle = captainHandle
        self.hasTeam = hasTeam
        self.captaininstances = captaininstances
    def createCSVString(self):
        ret_string=(self.player).createCSVString()
        return ret_string

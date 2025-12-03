class TeamCaptain:
    def __init__(self,captainHandle: str, player: object):
        self.player = player
        self.captainHandle = captainHandle
    def createCSVString(self):
        ret_string=(self.player).createCSVString()
        return ret_string

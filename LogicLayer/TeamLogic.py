from StorageLayer.storageApi import DataAPI
from Models.Team import Team

class Teamlogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass
    
    def getTeams(self) -> list[Team]:
        return self.__dataApi.loadTeams()

    def get_team_by_captain(self, captain_handle: str) -> Team | None:
        teams = self.getTeams()
        for team in teams:
            if team.get("captainHandle") == captain_handle:
                return team
        return None
    
    def createteam(self, team: list):
        teamID = team[0]
        teamName = team[1]
        roster = team[2]
        wins = team[3]
        losses = team[4]
        captainHandle = team[5]
        team = Team(teamID, teamName, roster, wins, losses, captainHandle)
        self.__dataApi.saveTeams()
        return
    
    def updateCaptain(self, captainHandle):
        captains = self.__dataApi.loadCaptains()
        captainslist = captains
        for captain in captainslist:
            if captain.get('captainHandle') == captainHandle:
                index = captainslist.index(captain)
                edited_captain = captain
                edited_captain['hasTeam'] = True
        captainslist.pop(index)
        captainslist.insert(index,edited_captain)
        return self.__dataApi.saveCaptain(captainslist)
    
    def searchForTeam(self, teamname):
        allteams = self.__dataApi.loadTeams()
        teamlist = []

        for team in allteams:
            if team['teamName'] == teamname:
                teamlist.append(team)
        return teamlist


    #team_names = [t.teamName for t in teams]


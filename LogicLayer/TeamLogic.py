from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Player import Player
from Models.Team import Team

class Teamlogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__teammodel = Team
        self.__playermodel = Player
        
    
    def getTeams(self) -> list[Team]:
        raw_list = self.__dataApi.loadTeams()
        teamlist: list[Team] = self.__logichandler.loadmodels(self.__teammodel,raw_list)
        for team in teamlist:
            players=self.getTeamMembers(team)
            team.playerinstances=players
        return teamlist


    def get_team_by_captain(self, captain_handle: str):
        teams = self.getTeams()
        for team in teams:
            if team.get("captainHandle") == captain_handle:
                return team
        return None
    
    def createteam(self, team: list):
        
        return self.__logichandler.createModel(self.__teammodel,team)

    
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
        allteams = self.getTeams()
        for team in allteams:
            if teamname in team:
                return team
            
    def getTeamMembers(self, team: Team):
        ret_list = []
        raw_list = self.__dataApi.loadPlayers()
        playerlist: list[Player] = self.__logichandler.loadmodels(self.__playermodel,raw_list)
        for player in playerlist:
            if player.teamID == team.teamID:
                ret_list.append(player)
        return ret_list
            
    




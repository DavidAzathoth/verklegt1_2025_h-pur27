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
        """Returns a list of all teams as loaded Team models"""
        raw_list = self.__dataApi.loadTeams()
        teamlist: list[Team] = self.__logichandler.loadmodels(self.__teammodel,raw_list)
        for team in teamlist:
            players=self.getTeamMembers(team)
            team.playerinstances=players
        return teamlist

    def get_team_by_captain(self, captain_handle: str):
        """Returns the team the given captain handle belongs to"""
        teams = self.getTeams()
        for t in teams:
            if t.captainHandle.lower().strip() == captain_handle.lower().strip():
                players=self.getTeamMembers(t)
                t.playerinstances=players
                return t
        return None
    
    def get_team_by_teamname(self, teamname: str, tournament) -> Team | None:
        """Returns the team that the given team name belongs to, can provide loaded tournament model, or a list of teams"""
        if type(tournament) == list:
            teamlist = tournament
        else:
            teamlist = tournament.teams
        for team in teamlist:
            if team.teamName.lower().strip() == teamname.lower().strip():
                return team
        return None
    
    def get_team_by_teamID(self, teamid: str, teamlist: list[Team]) -> Team | None:
        """Iterates through given teamlist and returns the team that the given teamid belongs to"""
        if None in teamlist:
            return None
        for team in teamlist:
            if team.teamID.lower().strip() == teamid.lower().strip():
                return team
        return None
        
    
    def createteam(self, team: list) -> Team:
        return self.__logichandler.createModel(self.__teammodel, team)
    
    def saveTeam(self, team: Team):
        """Adds Team to file"""
        self.__dataApi.saveTeam(team.createCSVDict())

    
    def updateCaptain(self, captainHandle):
        """Updates captain hasTeam status to True"""
        captainslist: list[dict] = self.__dataApi.loadCaptains()
        for captain in captainslist:
            if captain.get('captainHandle') == captainHandle:
                index = captainslist.index(captain)
                edited_captain = captain
                edited_captain['hasTeam'] = True
        captainslist.pop(index)
        captainslist.insert(index,edited_captain)
        return self.__dataApi.updateCaptains(captainslist)

    def registerCaptain(self, captainHandle):
        """Adds a new captain to the captains.csv file"""
        new_captain_info: dict = {"captainHandle":captainHandle, "hasTeam":False}
        self.__dataApi.saveCaptain(new_captain_info)
        return
            
    def getTeamMembers(self, team: Team):
        """Returns all team members of given team as a list of Player models"""
        ret_list = []
        raw_list = self.__dataApi.loadPlayers()
        playerlist: list[Player] = self.__logichandler.loadmodels(self.__playermodel,raw_list)
        for player in playerlist:
            if player.teamID == team.teamID:
                ret_list.append(player)
        return ret_list
    
    def updateTeam(self, input = None, operation: str = None, team: Team = None, amount = None):
        teams: list[dict]=self.__dataApi.loadTeams()

        for i, t in enumerate(teams):
            if str(t["teamID"]) == str(team.teamID):
                index = i
                break
        
        teams.pop(index)

        if team.roster and team.roster[0] == '':  #Clean empty string from list
            team.roster.pop(0)
        if operation=='addplayers':
            for player in input:
                player: Player
                team.roster.append(player.playerGamertag)
                team.playerinstances.append(player)
        elif operation=='updatewins':
            team.wins+=1
        elif operation=='updatelosses':
            team.losses+=1
        
        teams.insert(index, team.createCSVDict())

        self.__dataApi.updateTeams(teams)
            
        return team

    def getCaptain(self, captain_input: str):
        raw_list: list[dict] = self.__dataApi.loadCaptains()
        for c in raw_list:
            if (c.get('captainHandle')).lower().strip() == captain_input.lower().strip():
                return c
        return False
            
    



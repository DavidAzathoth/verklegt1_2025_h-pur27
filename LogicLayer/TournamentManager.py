from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Tournament import Tournament
from Models.Team import Team
from LogicLayer.TeamLogic import Teamlogic
class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__tournamentmodel = Tournament
        self.__teamlogic = Teamlogic(self.__dataApi)
        

    def createTournament(self, tournament: list):
        return self.__logichandler.createModel(self.__tournamentmodel,tournament)


    def getTournaments(self):
        raw_list = self.__dataApi.loadTournaments()
        tournamentlist: list[Tournament] = self.__logichandler.loadmodels(self.__tournamentmodel, raw_list)
        return tournamentlist
    
    def getTournamentbyName(self, name: str, tournamentlist: list[Tournament]):
        for tournament in tournamentlist:
            if name.lower().strip() == tournament.name.lower().strip():
                return tournament
            
    def populateTournament(self, tournament: Tournament):
        teams = self.__teamlogic.getTeams()
        #matches = implement this perhaps
        teamobjects=list(map(lambda team: self.__teamlogic.get_team_by_teamid(team, teams), (tournament.teams)))
        tournament.teams=teamobjects
        return tournament

        
    def saveTournament(self,tournament: Tournament):
        self.__dataApi.saveTournament(tournament.createCSVDict())
        return
    
    def updateTournament(self, tournament: Tournament, input: object, operation: str = None ):
        tournaments = self.__dataApi.loadTournaments()
        index = tournaments.index(tournament.createCSVDict())
        rem_tournament=tournament.createCSVDict()
        tournaments.remove(rem_tournament)

        if tournament.teams[0] == '': #Cleans up empty string that appears when list is first created
            tournament.teams.pop(0)
        if tournament.matchesList[0] == '':
            tournament.matchesList.pop(0)
        if tournament.matchHistory[0] == '':
            tournament.matchHistory.pop(0)

        if operation == 'addteam':
            if self.checkDuplTeams(tournament, input) == False:
                return False
            tournament.teams.append(input.teamID)
            tournament.teaminstances.append(input)
        
        tournaments.insert(index, tournament.createCSVDict())
        self.__dataApi.updateTournaments(tournaments)

    def addTeamtoTournament(self, tournament: Tournament, team: Team):
        if self.checkDuplTeams(tournament, team):
            tournament.teams.append(team)

    def checkDuplTeams(self, tournament: Tournament, team: Team):
        reg_team : Team
        for reg_team in tournament.teams:
            if reg_team.teamID == team.teamID:
                return False
        return True


#    def calculaterounds(self, teams: list[Team]):
#        oddrounds = 0
#        totalrounds = 0
#        divbytwo = len(teams)
#        while divbytwo != 1:
#            temp=divbytwo / 2
#            if divbytwo / 2 != 0:
#                oddrounds += 1
#                divbytwo=divbytwo-1

#            
        


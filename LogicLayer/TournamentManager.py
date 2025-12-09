from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Bracket import Bracket
from LogicLayer.TeamLogic import Teamlogic
from LogicLayer.MatchLogic import MatchLogic
class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__tournamentmodel = Tournament
        self.__teamlogic = Teamlogic(self.__dataApi)
        self.__matchlogic = MatchLogic(self.__dataApi)
        

    def createTournament(self, tournament: list):
        return self.__logichandler.createModel(self.__tournamentmodel,tournament)


    def getTournaments(self):
        raw_list = self.__dataApi.loadTournaments()
        tournamentlist: list[Tournament] = self.__logichandler.loadmodels(self.__tournamentmodel, raw_list)
        return tournamentlist
    
    def getTournamentbyName(self, name: str, tournamentlist: list[Tournament]):
        for tournament in tournamentlist:
            if name==tournament.name:
                return tournament
            
    def populateTournament(self, tournament: Tournament):
        teams = self.__teamlogic.getTeams()
        teamobjects=list(map(lambda team: self.__teamlogic.get_team_by_teamID(team, teams), (tournament.teams)))
        tournament.teams=teamobjects
        return tournament
    def unpopulateTournament(self, tournament: Tournament):
        teamids = [x.teamID for x in tournament.teams]
        tournament.teams=teamids
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
    
    def populateBracket(self, bracket: Bracket):
        matches = self.__matchlogic.getMatches()
        rounds: dict[list]
        for round in bracket.rounds.keys():
            roundobjects = list(map(self.__matchlogic.getMatchbyID, bracket.rounds[round]))
            print(roundobjects)
            print(bracket.rounds)
        return bracket
    

    def availableteams(self, tournament : Tournament):
        all_teams = self.__teamlogic.getTeams()
        teamIDs = []
        for tID in tournament.teams:
            tID = tID.strip()
            if tID != "":
                teamIDs.append(tID)
        available = []
        for team in all_teams:
            if team.teamID not in teamIDs:
                available.append(team)    
        return available
    

    ###NOT IMPLEMENTED TODO


    def unpopulateBracket(self, bracket):
        matchids=self.__dataApi.loadMatches()

#def populateTournament(self, tournament: Tournament):
#        teams = self.__teamlogic.getTeams()
#        teamobjects=list(map(lambda team: self.__teamlogic.get_team_by_teamID(team, teams), (tournament.teams)))
#        tournament.teams=teamobjects
#        return tournament


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
        


from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Bracket import Bracket
from Models.Match import Match
from LogicLayer.TeamLogic import Teamlogic
from LogicLayer.MatchLogic import MatchLogic
class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__tournamentmodel = Tournament
        self.__bracketmodel = Bracket
        self.__matchmodel = Match
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
            if name.lower().strip() == tournament.name.lower().strip():
                return tournament
            
    def populateTournament(self, tournament: Tournament):
        teams = self.__teamlogic.getTeams()
        teamobjects=list(map(lambda team: self.__teamlogic.get_team_by_teamID(team, teams), (tournament.teams)))
        bracket = self.getBracketByTournament(tournament)
        tournament.bracket = bracket
        tournament.teams = teamobjects

        return tournament
    
    def unpopulateTournament(self, tournament: Tournament):
        teamids = [x.teamID for x in tournament.teams]
        tournament.teams=teamids
        return tournament
    
    
        
    def saveTournament(self,tournament: Tournament):
        self.unpopulateTournament(tournament)
        self.__dataApi.saveTournament(tournament.createCSVDict())
        return
    
    def updateTournament(self, tournament: Tournament, input: object = None, operation: str = None ):
        if tournament.active==False:
            return False
        tournaments = self.getTournaments()
        for t in tournaments:
            if tournament.name == t.name:
                index = tournaments.index(t)
                break
        tournaments.remove(t)

        if tournament.teams[0] == '': #Cleans up empty string that appears when list is first created
            tournament.teams.pop(0)
        if tournament.matchesList[0] == '':
            tournament.matchesList.pop(0)
        if tournament.matchHistory[0] == '':
            tournament.matchHistory.pop(0)

        if operation == 'addteam':
            if self.checkDuplTeams(tournament, input) == False:
                return False
            tournament.teams.append(input)
        if operation == 'updateall':
            self.updateBracket(tournament.bracket)
            for team in tournament.teams:
                self.__teamlogic.updateTeam(None,None,team)

        self.unpopulateTournament(tournament)
        tournaments.insert(index, tournament)
        tournaments=[t.createCSVDict() for t in tournaments]
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
    
    def getBrackets(self)->list[Bracket]:
        raw_list = self.__dataApi.loadBrackets()
        bracketlist: list[Bracket] = self.__logichandler.loadmodels(self.__bracketmodel, raw_list)
        for bracket in bracketlist:
            bracket.rounds=eval(bracket.rounds)
        return bracketlist
    
    def getBracketByTournament(self,tournament: Tournament):
        bracketlist = self.getBrackets()
        bracket: Bracket
        for bracket in bracketlist:
            if bracket.tournamentname==tournament.name:
                self.populateBracket(bracket)
                return bracket
        return
            

    def saveBracket(self, bracket: Bracket):
        bracket=self.unpopulateBracket(bracket)
        self.__dataApi.saveBracket(bracket.createCSVDict())


    def populateBracket(self, bracket: Bracket):
        rounds: dict[list]
        for round in bracket.rounds.keys():
            roundobjects = list(map(self.__matchlogic.getMatchbyID, bracket.rounds.get(round)))
            bracket.rounds[round]=roundobjects
        return bracket


    def unpopulateBracket(self, bracket: Bracket):
        for round in bracket.rounds.keys():
            matchids=[match.matchID for match in bracket.rounds.get(round)]
            bracket.rounds[round] = matchids
        return bracket
    
    def updateBracket(self, bracket: Bracket):
        for round in bracket.rounds.keys():
            for match in bracket.rounds.get(round):
                self.__matchlogic.updateMatch(match)


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
        


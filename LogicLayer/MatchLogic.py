from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Match import Match
class MatchLogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__matchmodel = Match
    def getMatchesCSV(self):
        matches = self.__dataApi.loadMatches()
        return matches

    def getMatches(self):
        raw_list = self.__dataApi.loadMatches()
        matchlist: list[Match] = self.__logichandler.loadmodels(self.__matchmodel, raw_list)
        return matchlist
    
    def getMatchbyID(self, id: str):
        matchlist = self.getMatches()
        for match in matchlist:
            if match.matchID == id:
                return match
        return None
    def updateMatch(self, match: Match):
        matches = self.getMatchesCSV
        pass



# def updateTournament(self, tournament: Tournament, input: object, operation: str = None ):
#        tournaments = self.__dataApi.loadTournaments()
#        index = tournaments.index(tournament.createCSVDict())
#        rem_tournament=tournament.createCSVDict()
#        tournaments.remove(rem_tournament)
#
#        if tournament.teams[0] == '': #Cleans up empty string that appears when list is first created
#            tournament.teams.pop(0)
#        if tournament.matchesList[0] == '':
#            tournament.matchesList.pop(0)
#        if tournament.matchHistory[0] == '':
#            tournament.matchHistory.pop(0)
#
#        if operation == 'addteam':
#            if self.checkDuplTeams(tournament, input) == False:
#                return False
#            tournament.teams.append(input.teamID)
#            tournament.teaminstances.append(input)
#        
#        tournaments.insert(index, tournament.createCSVDict())
#        self.__dataApi.updateTournaments(tournaments)
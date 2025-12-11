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
        for match in matchlist:
            match.Score = eval(match.Score)
        return matchlist
    
    def getMatchbyID(self, id: str):
        matchlist = self.getMatches()
        for match in matchlist:
            if match.matchID == id:
                return match
        return None
    




    def updateMatch(self, editedmatch: Match, input = None, operation: str = None):
        matches = self.getMatches()
        for match in matches:
            if match.matchID == editedmatch.matchID:
                index = matches.index(match)
                matches.remove(match)
                matches.insert(index, editedmatch)
        
        data = [match.createCSVDict() for match in matches]
        self.__dataApi.updateMatch(data)

    def returnMatchWinnerconfirmation(self, match: Match, scores: list):
        """Returns winner from list, list is team_A score for index 0 and team_B score for index 1 [0,1].
        Does not save to file or update any data."""
        if scores[0]>scores[1]:
            return match.team_A
        else:
            return match.team_B
    def confirmMatchWinner(self, match: Match, scores: list):
        """Input scores is a list [1,2] score 1(index 0) is team_A score and score 2(index 1) is team_B score"""
        raw_dict={f'{match.team_A}':f'{scores[0]}',f'{match.team_B}':f'{scores[1]}'}
        if scores[0]>scores[1]:
            match.matchWinner = match.team_A
            matchloser = match.team_B
        else:
            match.matchWinner = match.team_B
            matchloser = match.team_A
        match.Score=raw_dict
        match.matchPlayed=True
        return matchloser, match.matchWinner
        
        
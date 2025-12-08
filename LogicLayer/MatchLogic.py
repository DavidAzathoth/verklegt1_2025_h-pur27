from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Match import Match
class MatchLogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__matchmodel = Match
    
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

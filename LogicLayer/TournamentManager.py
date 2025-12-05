from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Tournament import Tournament
from Models.Team import Team
class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__tournamentmodel = Tournament
        pass

    def createTournament(self, tournament: list):
        return self.__logichandler.createModel(self.__tournamentmodel,tournament)


    def getTournament(self):
        return self.__dataApi.loadTournaments()
    
    def saveTournament(self,tournament: Tournament):
        self.__dataApi.saveTournament(tournament.createCSVDict())
        return
    def calculaterounds(self, teams: list[Team]):
        oddrounds = 0
        totalrounds = 0
        divbytwo = len(teams)
        while divbytwo != 1:
            temp=divbytwo / 2
            if divbytwo / 2 != 0:
                oddrounds += 1
                divbytwo=divbytwo-1
            
        


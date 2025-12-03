from StorageLayer.storageHandler import StorageHandler
from Models.Team import Team

class DataAPI:
    def __init__(self):
        self.__storagehandler=StorageHandler()
    def loadTeams(self):
        ret = self.__storagehandler.retrieveFile("Storagelayer/Data/teams.csv")
        if ret:
            return ret
        else:
            return False
    def saveTeams(self, addition):
        self.__storagehandler.saveFile(addition,'teams')
        return
    def loadTournaments(self):
        return self.__storagehandler.retrieveFile("Storagelayer/Data/tournaments.csv")
    def saveTournaments(self,addition):
        self.__storagehandler.saveFile(addition,'tournaments')
from StorageLayer.storageApi import DataAPI
class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass

    def createTournament(self):
        return self.__dataApi.saveTournament()


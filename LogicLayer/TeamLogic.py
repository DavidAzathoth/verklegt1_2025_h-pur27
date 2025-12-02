from StorageLayer.storageApi import DataAPI
class Teamlogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass
    def getTeams(self):
        return self.__dataApi.loadTeams()

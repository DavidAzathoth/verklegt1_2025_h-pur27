from StorageLayer.storageHandler import StorageHandler

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
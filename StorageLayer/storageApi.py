from StorageLayer.storageHandler import StorageHandler

class DataAPI:
    def __init__(self):
        self.file="Storagelayer/Data/teams.csv"
        self.__storagehandler=StorageHandler()
    def loadTeams(self):
        ret = self.__storagehandler.retrieveFile(self.file)
        if ret:
            return ret
        else:
            return False
    def saveTeams(self):
        self.__storagehandler.saveFile(self.file)
        return
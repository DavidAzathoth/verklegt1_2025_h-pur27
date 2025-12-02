from StorageLayer.storageHandler import StorageHandler

class DataAPI:
    def __init__(self):
        self.__storagehandler=StorageHandler()
    def loadTeams(self,file: str):
        ret = self.__storagehandler.retrieveFile(file)
        if ret:
            return ret
        else:
            return False
    def saveTeams(self,file: str):
        self.__storagehandler.saveFile(file)
        return
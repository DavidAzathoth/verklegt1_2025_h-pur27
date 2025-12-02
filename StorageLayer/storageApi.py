from StorageLayer.storageHandler import StorageHandler
class DataAPI:
    def __init__(self):
        pass
    def loadTeams(self):
        #REMOVE HARDCODED FILE PATH
        return StorageHandler().retrieveFile("StorageLayer/Data/teams.csv")
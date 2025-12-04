from StorageLayer.storageHandler import StorageHandler
class PlayerData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/players.csv'
        self.__storagehandler = storagehandler
    def load_players(self):
        return self.__storagehandler.retrieveFile(self.FILE)
    def savePlayer(self,data):
        self.__storagehandler.saveFile(self.FILE,data)
        return
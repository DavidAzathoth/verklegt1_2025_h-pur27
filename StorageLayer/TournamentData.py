from StorageLayer.storageHandler import StorageHandler
class TournamentData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE='StorageLayer/Data/tournaments.csv'
        self.__storagehandler = storagehandler
    def load_tournaments(self):
        return self.__storagehandler.retrieveFile(self.FILE)
    def save_tournament(self,data):
        self.__storagehandler.saveFile(self.FILE,data)
        return
    def update_tournaments(self, data):
        self.__storagehandler.editFile(self.FILE, data)
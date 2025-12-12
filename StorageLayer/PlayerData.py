from StorageLayer.storageHandler import StorageHandler
class PlayerData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/players.csv'
        self.__storagehandler = storagehandler
    def load_players(self):
        """Loads players from file and returns a list of dictionaries"""
        return self.__storagehandler.retrieveFile(self.FILE)
    def savePlayer(self,data):
        """Adds player to file"""
        self.__storagehandler.saveFile(self.FILE,data)
        return
    def updatePlayers(self,data):
        """Similar to update_tournaments (see TournamentData.update_tournaments)"""
        self.__storagehandler.editFile(self.FILE,data)
        return
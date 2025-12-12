from StorageLayer.storageHandler import StorageHandler
class TournamentData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE='StorageLayer/Data/tournaments.csv'
        self.__storagehandler = storagehandler
    def load_tournaments(self):
        """Loads all tournaments from and returns as a list of dictionaries"""
        return self.__storagehandler.retrieveFile(self.FILE)
    def save_tournament(self,data):
        """Adds tournament to file"""
        self.__storagehandler.saveFile(self.FILE,data)
        return
    def update_tournaments(self, data):
        """Updates given list of tournaments, replacing the whole tournament file with this list. The list is created in the logic layer"""
        self.__storagehandler.editFile(self.FILE, data)

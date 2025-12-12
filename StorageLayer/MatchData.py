from StorageLayer.storageHandler import StorageHandler
class MatchData:
    def __init__(self, storagehandler: StorageHandler):
        self.__storagehandler = storagehandler
        self.FILE = 'StorageLayer/Data/matches.csv'
    def load_matches(self):
        """Loads matches from file and returns a list of dictionaries"""
        return self.__storagehandler.retrieveFile(self.FILE)
    def save_match(self, data):
        """Adds match to file"""
        self.__storagehandler.saveFile(self.FILE, data)
        return
    def update_match(self, data):
        """Similar to update_tournaments (see TournamentData.update_tournaments)"""
        self.__storagehandler.editFile(self.FILE, data)

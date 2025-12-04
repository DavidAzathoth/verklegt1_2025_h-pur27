from StorageLayer.storageHandler import StorageHandler
class MatchData:
    def __init__(self, storagehandler: StorageHandler):
        self.__storagehandler = storagehandler
        self.FILE = 'StorageLayer/Data/matches.csv'
    def load_matches(self):
        return self.__storagehandler.retrieveFile(self.FILE)
    def save_match(self, data):
        self.__storagehandler.saveFile(self, data)
        return
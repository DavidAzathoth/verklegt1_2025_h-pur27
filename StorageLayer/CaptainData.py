from StorageLayer.storageHandler import StorageHandler
class CaptainData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/captains.csv'
        self.__storagehandler = storagehandler
    def load_captains(self):
        """Loads captains from file and returns a list of dictionaries"""
        return self.__storagehandler.retrieveFile(self.FILE)
    def update_captains(self,data):
        """Similar to update_tournaments (see TournamentData.update_tournaments)"""
        self.__storagehandler.editFile(self.FILE,data)
    def save_captain(self,data):
        """Adds captain to file"""
        self.__storagehandler.saveFile(self.FILE,data)
        return        

from StorageLayer.storageHandler import StorageHandler
class TeamData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/teams.csv'
        self.__storagehandler = storagehandler
    def load_teams(self):
        """Loads teams from file and returns a list of dictionaries"""
        return self.__storagehandler.retrieveFile(self.FILE)
    def save_team(self,data):
        """Adds team to file"""
        self.__storagehandler.saveFile(self.FILE,data)
        return
    def update_team(self, data: list):
        """Similar to update_tournaments (see TournamentData.update_tournaments)"""
        self.__storagehandler.editFile(self.FILE, data)
        return
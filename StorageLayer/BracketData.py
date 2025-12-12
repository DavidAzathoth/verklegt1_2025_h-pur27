from StorageLayer.storageHandler import StorageHandler
class BracketData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/bracket.csv'
        self.__storagehandler = storagehandler

    def loadBrackets(self):
        """Loads brackets from file and returns a list of dictionaries"""
        return self.__storagehandler.retrieveFile(self.FILE)
    def saveBracket(self, bracket):
        """Adds bracket to file"""
        self.__storagehandler.saveFile(self.FILE, bracket)

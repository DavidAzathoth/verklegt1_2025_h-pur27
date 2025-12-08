from StorageLayer.storageHandler import StorageHandler
class BracketData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/bracket.csv'
        self.__storagehandler = storagehandler

    def loadBrackets(self):
        return self.__storagehandler.retrieveFile(self.FILE)
    def saveBracket(self, bracket):
        self.__storagehandler.saveFile(self.FILE, bracket)

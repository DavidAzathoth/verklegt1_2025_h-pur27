from StorageLayer.storageHandler import StorageHandler
class CaptainData:
    def __init__(self, storagehandler: StorageHandler):
        self.FILE = 'StorageLayer/Data/captains.csv'
        self.__storagehandler = storagehandler
    def load_captains(self):
        return self.__storagehandler.retrieveFile(self.FILE)
    def update_captains(self,data):
        self.__storagehandler.editFile(self.FILE,data)

from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Player import Player

class Playerlogic:
    def __init__(self, dataApi: DataAPI):
        self.PLAYERATTRIBUTES = ['teamID','playerGamertag','fullname','phoneNumber','emailAddress','address','link']
        self.__logichandler = logicHandler()
        self.__dataApi = dataApi
        self.__playermodel = Player
        

    def createplayer(self, player: list):
        return self.__logichandler.createModel(self.__playermodel,player)


        
    def getplayers(self):
        raw_data = self.__dataApi.loadPlayers()
        playerlist=self.__logichandler.loadmodels(self.__playermodel,raw_data)
        return playerlist
    
    def saveplayer(self, player: Player):
        self.__dataApi.savePlayer(player.createCSVDict())
        return
    def getplayer_by_gamertag(self, tag):
        players: list[Player] = self.getplayers()
        for player in players:
            if player.playerGamertag==tag:
                return player
    def editplayer(self, attribute: str):
        if attribute in self.PLAYERATTRIBUTES:
            pass 
        #TODO IMPLEMENT

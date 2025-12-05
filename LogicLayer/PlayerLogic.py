from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Player import Player

class Playerlogic:
    def __init__(self, dataApi: DataAPI):
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


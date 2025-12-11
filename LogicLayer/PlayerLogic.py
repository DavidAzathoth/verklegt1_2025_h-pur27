from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Player import Player
from LogicLayer.menuLogic import MenuLogic

class Playerlogic:
    def __init__(self, dataApi: DataAPI):
        self.PLAYERATTRIBUTES = ['teamID','playerGamertag','fullname','phoneNumber','emailAddress','address','link']
        self.__logichandler = logicHandler()
        self.__dataApi = dataApi
        self.__menulogic = MenuLogic(DataAPI)
        self.__playermodel = Player
        

    def createplayer(self, player: list) -> Player:
        return self.__logichandler.createModel(self.__playermodel,player)


        
    def getplayers(self):
        raw_data = self.__dataApi.loadPlayers()
        playerlist: list [Player] = self.__logichandler.loadmodels(self.__playermodel,raw_data)
        return playerlist
    
    def saveplayer(self, player: Player):
        self.__dataApi.savePlayer(player.createCSVDict())
        return
    
    def getplayer_by_gamertag(self, tag: str):
        players: list[Player] = self.getplayers()
        for player in players:
            if player.playerGamertag.lower().strip() == tag.lower().strip():
                return player
            
    def editplayer(self, gamertag: str, attribute: str, newValue: str):
        if attribute in self.PLAYERATTRIBUTES:
            players = self.getplayers()
            for p in players:
                if p.playerGamertag == gamertag:
                    
                    if attribute == "phoneNumber":
                        p.phoneNumber = newValue
                    elif attribute == "emailAddress":
                        check_player_email: tuple = self.__menulogic.emailverification(newValue)
                        if check_player_email[1] == False:
                            return check_player_email
                        p.emailAddress = check_player_email[0]
                    elif attribute == "address":
                        p.address = newValue
                    elif attribute == "link":
                        p.link = newValue
                    
                    data = [pl.createCSVDict() for pl in players]
                    self.__dataApi.updatePlayers(data)
                    return True
        return False    

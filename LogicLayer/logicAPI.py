from LogicLayer.TeamLogic import Teamlogic
from LogicLayer.menuLogic import MenuLogic
from StorageLayer.storageApi import DataAPI


class LogicAPI:
    def __init__(self):
        dataAPI: DataAPI = DataAPI()
        self.__Menulogic = MenuLogic(dataAPI)
        self.Teamlogic = Teamlogic(dataAPI)
        

        return

    def createteam(self, input: dict):
        return self.__Teamlogic.createteam(input)
    
    def showTeams(self):
        return self.__Menulogic.showTeams()
    
    def getTeams(self) -> list[dict]:
        return self.Teamlogic.getTeams()

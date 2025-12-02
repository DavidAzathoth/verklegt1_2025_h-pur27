from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI


class LogicAPI:
    def __init__(self, Teamlogic: Teamlogic, DataAPI: DataAPI):
        self.__Teamlogic = Teamlogic
        self.__DataAPI = DataAPI
        return

    def createteam(self, input: dict):
        return self.__Teamlogic.createteam(input)
    
    
    
    def temp(self):
        return DataAPI.loadTeams()

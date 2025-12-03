from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI
from LogicLayer.TournamentManager import Tournamentmanager


class LogicAPI:
    def __init__(self, Teamlogic: Teamlogic, DataAPI: DataAPI, Tournamentmanager: Tournamentmanager):
        self.__Teamlogic = Teamlogic
        self.__Menulogic = MenuLogic(dataAPI)
        self.__DataAPI = DataAPI
        self.__Tournamentmanager = Tournamentmanager
        return

    def createteam(self, input: dict):
        return self.__Teamlogic.createteam(input)
    
    def showTeams(self):
        return self.__Menulogic.showTeams()
    
    def getTeams(self) -> list[dict]:
        return self.__Teamlogic.getTeams()

    def get_team_by_captain(self, captain_handle: str):
        return self.__Teamlogic.get_team_by_captain(captain_handle)
    
    def temp(self):
        return DataAPI.loadTeams()
    
    
    
    
    
    
    
    
    def createtournament(self, input):
        templist = ["HA", "HAringurinn", "20 12 2025", "24 12 2025", "blabla@gmail.com", "1234567"]
        #TODO check tournament for duplicates
        return self.__Tournamentmanager.createtournament(input)


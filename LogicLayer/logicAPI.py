from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI
from LogicLayer.TournamentManager import Tournamentmanager
from LogicLayer.menuLogic import MenuLogic

class LogicAPI:
    def __init__(self):
        __dataAPI = DataAPI()
        self.__Teamlogic = Teamlogic(__dataAPI)
        self.__Menulogic = MenuLogic(__dataAPI)
        self.__Tournamentmanager = Tournamentmanager(__dataAPI)
        return

    def createteam(self, input: dict):
        return self.__Teamlogic.createteam(input)
        #not implemented#
    
    def showTeams(self):
        return self.__Menulogic.showTeams()
    
    
    def temp(self):
        return DataAPI.loadTeams()
    
    
    def createtournament(self, input):
        templist = ["HA", "HAringurinn", "20 12 2025", "24 12 2025", "blabla@gmail.com", "1234567"]
        #TODO check tournament for duplicates
        return self.__Tournamentmanager.createTournament(input)


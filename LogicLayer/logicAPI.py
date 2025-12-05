from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI
from LogicLayer.TournamentManager import Tournamentmanager
from LogicLayer.menuLogic import MenuLogic
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Player import Player
from LogicLayer.PlayerLogic import Playerlogic

class LogicAPI:
    def __init__(self):
        __dataAPI = DataAPI()
        self.__Teamlogic = Teamlogic(__dataAPI)
        self.__Menulogic = MenuLogic(__dataAPI)
        self.__Tournamentmanager = Tournamentmanager(__dataAPI)
        self.__Playerlogic = Playerlogic(__dataAPI)
        return

    def createteam(self, input: dict):
        return self.__Teamlogic.createteam(input)
        
    
    def showTeams(self):
        return self.__Menulogic.showTeams()
    
    def getTeams(self) -> list[Team]:
        return self.__Teamlogic.getTeams()

    def get_team_by_captain(self, captain_handle: str):
        return self.__Teamlogic.get_team_by_captain(captain_handle)
    
    def temp(self):
        return DataAPI.loadTeams()
    
    def gettournament(self):
        return self.__Tournamentmanager.getTournament()

    def createtournament(self, input):
        templist = ["HA", "HAringurinn", "20 12 2025", "24 12 2025", "blabla@gmail.com", "1234567"]
        #TODO check tournament for duplicates
        return self.__Tournamentmanager.createTournament(input)
    def saveTournament(self, tournament: Tournament):
        self.__Tournamentmanager.saveTournament(tournament)
        return
    
    def updatecaptain(self, input):
        return self.__Teamlogic.updateCaptain(input)

    def searchforteam(self, input):
        return self.__Teamlogic.searchForTeams(input)
    
    def createPlayer(self, input):
        return self.__Playerlogic.createplayer(input)
    
    def getPlayers(self):
        return self.__Playerlogic.getplayers()
    
    def savePlayer(self, player: Player):
        self.__Playerlogic.saveplayer(player)

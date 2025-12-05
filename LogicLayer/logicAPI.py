from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI
from LogicLayer.TournamentManager import Tournamentmanager
from LogicLayer.menuLogic import MenuLogic
from LogicLayer.BracketGenerator import BracketGenerator
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
        self.__bracketgenerator = BracketGenerator()
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
        """Updates given captain in file"""
        return self.__Teamlogic.updateCaptain(input)

    def searchforteam(self, input):
        return self.__Teamlogic.searchForTeams(input)
    
    def createPlayer(self, input):
        """Creates a player, does not automatically store in file"""
        return self.__Playerlogic.createplayer(input)
    
    def getPlayer_by_gamertag(self, gamertag: str):
        """Returns player object with matching gamertag"""
        return self.__Playerlogic.getplayer_by_gamertag(gamertag)
    
    def getPlayers(self):
        """Returns all players stored in file"""
        return self.__Playerlogic.getplayers()
    
    def savePlayer(self, player: Player):
        """Store player to file"""
        self.__Playerlogic.saveplayer(player)
    def getPlayer_teamID(self):
        """# Not implemented #"""
        #NOT IMPLEMENTED
        players = self.getPlayers()

    def emailVerification(self, email):
        """Verifies if email is valid"""
        return self.__Menulogic.emailverification(email)
    
    def addplayer(self, input: list, team: Team):
        """Adds player to team. Input is a list to generate the player and team is the team object"""
        return self.__Teamlogic.addplayertoteam(input, team)

    def validateTeam(self, team: Team):
        """Returns False if team has reached maximum players (5)"""
        if len(team.roster)==5:
            return False
    def updatescore(self, team: Team, option: str):
        """Updates win or losses of team, options are updatewins and updatelosses"""
        self.__Teamlogic.updateTeam(None, option, team)
        return
    def generatebracket(self, teams):
        return self.__bracketgenerator.generatebracket(teams)

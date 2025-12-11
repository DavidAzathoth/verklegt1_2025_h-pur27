from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI
from LogicLayer.TournamentManager import Tournamentmanager
from LogicLayer.menuLogic import MenuLogic
from LogicLayer.BracketGenerator import BracketGenerator
from LogicLayer.MatchLogic import MatchLogic
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Player import Player
from Models.Match import Match
from LogicLayer.PlayerLogic import Playerlogic
from LogicLayer.BracketLogic import BracketLogic

class LogicAPI:
    def __init__(self):
        __dataAPI = DataAPI()
        self.__Teamlogic = Teamlogic(__dataAPI)
        self.__Menulogic = MenuLogic(__dataAPI)
        self.__Tournamentmanager = Tournamentmanager(__dataAPI)
        self.__Playerlogic = Playerlogic(__dataAPI)
        self.__bracketgenerator = BracketGenerator()
        self.__matchlogic = MatchLogic(__dataAPI)
        self.__bracketlogic = BracketLogic()
        return

    def createteam(self, input: list):
        return self.__Teamlogic.createteam(input)
        
    
    def showTeams(self):
        return self.__Menulogic.showTeams()
    
    def getTeams(self) -> list[Team]:
        return self.__Teamlogic.getTeams()

    def get_team_by_captain(self, captain_handle: str):
        return self.__Teamlogic.get_team_by_captain(captain_handle)
    
    
    def gettournaments(self):
        return self.__Tournamentmanager.getTournaments()

    def getTournamentbyName(self, name: str):
        tournaments = self.__Tournamentmanager.getTournaments()
        return self.__Tournamentmanager.getTournamentbyName(name, tournaments)

    def populateTournament(self, tournament: Tournament):
        """Populates tournament with all objects and returns it, must give tournament name and already loaded list of tournament objects"""
        self.__Tournamentmanager.populateTournament(tournament)
        
    def unpopulateTournament(self, tournament: Tournament):
        self.__Tournamentmanager.unpopulateTournament(tournament)

    def createtournament(self, input):
        """Attempts to create a tournament, returns False if a tournamentn with the same name inputted already exists"""
        name = input[1]
        existing_tournaments = self.__Tournamentmanager.getTournaments()
        for tournament in existing_tournaments:
            if tournament.name == name:
                return False
        return self.__Tournamentmanager.createTournament(input)
    
    def saveTournament(self, tournament: Tournament):
        self.__Tournamentmanager.saveTournament(tournament)
        return
    def updateTournament(self, tournament: Tournament,):
        """Updates all information about tournament, brackets, matches, teams and overwrites the files with the updated information"""
        self.__Tournamentmanager.updateTournament(tournament,None, 'updateall')
    
    def addTeamtoTournament(self, team: Team,tournament: Tournament):
        """Adds team to tournament, both parameters must be an object. Returns false if the team is already in the tournament"""
        self.__Tournamentmanager.updateTournament(tournament, team, 'addteam')
    
    def updatecaptain(self, input):
        """Updates given captain in file"""
        return self.__Teamlogic.updateCaptain(input)
    
    def getCaptain(self, captainHandle: str):
        return self.__Teamlogic.getCaptain(captainHandle)
    
    def registerCaptain(self, captainHandle):
        return self.__Teamlogic.registerCaptain(captainHandle)
    
    #def getTournamentbyName(self, name: str):
    #    tournamentlist = self.__Tournamentmanager.getTournaments()
    #    return self.__Tournamentmanager.getTournamentbyName(name, tournamentlist)

    def searchforteam(self, input):
        teams=self.__Teamlogic.getTeams()
        return self.__Teamlogic.get_team_by_teamname(input, teams)
    
    def createPlayer(self, input: list) -> Player:
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
        teams = self.getTeams()
        players = self.getPlayers()

    def editplayer(self, gamertag: str, attribute: str, newValue: str):
        self.__Playerlogic.editplayer(gamertag, attribute, newValue)

    def emailVerification(self, email):
        """Verifies if email is valid"""
        return self.__Menulogic.emailverification(email)
    
    def addplayers(self, players: list[Player], team: Team):
        """Adds players to team. players is a list to generate the player and team is the team object"""
        return self.__Teamlogic.updateTeam(players, 'addplayers', team)

    def validateTeam(self, team: Team):
        """Returns False if team has reached maximum players (5)"""
        if len(team.roster)==5:
            return False
    def updatescore(self, team: Team, option: str, amount: int = None):
        """Updates win or losses of team, options are updatewins and updatelosses
        \noptions: 'updatewins', 'updatelosses'"""
        self.__Teamlogic.updateTeam(None, option, team, amount)
        return
    
    def generatebracket(self, tournament):
        return self.__bracketgenerator.generatebracket(tournament)
    
    def roundsplayed(self, teams):
        return self.__bracketgenerator.playingames(teams)
    
    def getMatchbyID(self, id: str):
        return self.__matchlogic.getMatchbyID(id)
      
    def updateMatchWinner(self, match, team):
        self.__matchlogic.updateMatch(match, team, 'updatewinner')

    
    def availableteams(self, tournament : Tournament):
        return self.__Tournamentmanager.availableteams(tournament)
      
    def saveBracket(self, bracket):
        self.__Tournamentmanager.saveBracket(bracket)

    def saveTeam(self, team: Team):
        self.__Teamlogic.saveTeam(team)
    
    def updateBracket(self, tournament):
        self.__bracketgenerator.updatebracket(tournament)
        self.__Tournamentmanager.updateTournament(tournament,None ,'updateall')
    
    def updateOrMatches(self, tournament: Tournament, matchwinner: str):
        self.__bracketgenerator.updateOrMatches(tournament, matchwinner)
        return


    def returnMatchWinner(self, match, scores):
        return self.__matchlogic.returnMatchWinnerconfirmation(match, scores)
    
    def confirmMatchWinner(self, match: Match, scores)-> tuple[str,str]:
        """Input scores is a list [1,2] score 1(index 0) is team_A score and score 2(index 1) is team_B score
        To update the bracket correctly use these commands in this order \n
        matchloser, matchwinner = llapi.confirmMatchWinner(match, score) \n
        llapi.removeTeamfromTournament(tournament, matchloser) \n
        llapi.updateOrMatches(tournament,matchwinner) \n
        llapi.updateBracket(tournament)
        """
        matchloser, matchwinner = self.__matchlogic.confirmMatchWinner(match, scores)
        return matchloser, matchwinner
        
    def populateBracket(self, bracket):
        self.__Tournamentmanager.populateBracket(bracket)

    def removeTeamfromTournament(self, tournament: Tournament, teamname: str):
        """Removes team from tournament, input teamname. Meant to be used after updating matches with confirmMatchWinner in logic api"""
        self.__Tournamentmanager.removeTeamfromTournament(tournament, teamname)
        return
    def getNamedRounds(self, bracket):
        return self.__bracketlogic.getnamedrounds(bracket)
    
    def reloadTournament(self, tournament: Tournament):
        return self.__Tournamentmanager.reloadTournament
###############testing area#############

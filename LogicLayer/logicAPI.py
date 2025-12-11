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
        """Creates a team object from the input list and returns it"""
        return self.__Teamlogic.createteam(input)
        
    
    def getTeams(self) -> list[Team]:
        """Returns all teams as Team objects and loads players into their team"""
        return self.__Teamlogic.getTeams()

    def get_team_by_captain(self, captain_handle: str):
        """Returns the team that belongs to the given captain handle or None if not found"""
        return self.__Teamlogic.get_team_by_captain(captain_handle)
    
    
    def gettournaments(self):
        """Returns all tournaments as Tournament objects"""
        return self.__Tournamentmanager.getTournaments()

    def getTournamentbyName(self, name: str):
        """Return tournament with the given name or None if it doesn't exist yet"""
        tournaments = self.__Tournamentmanager.getTournaments()
        return self.__Tournamentmanager.getTournamentbyName(name, tournaments)

    def populateTournament(self, tournament: Tournament):
        """Populates tournament with all objects and returns it, must give tournament name and already loaded list of tournament objects"""
        self.__Tournamentmanager.populateTournament(tournament)
        
    def unpopulateTournament(self, tournament: Tournament):
        """Replaces team objects in Tournament with their IDs"""
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
        """Save tournament file after changing team objects back to IDs"""
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
        """Gets captain by handle"""
        return self.__Teamlogic.getCaptain(captainHandle)
    
    def registerCaptain(self, captainHandle):
        """Adds a new captain to the system"""
        return self.__Teamlogic.registerCaptain(captainHandle)
    
    #def getTournamentbyName(self, name: str):
    #    tournamentlist = self.__Tournamentmanager.getTournaments()
    #    return self.__Tournamentmanager.getTournamentbyName(name, tournamentlist)

    def searchforteam(self, input):
        """Return a team by name"""
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
        """Edits a player's information"""
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
        """Generate tournament bracket if it doesnt have one"""
        return self.__bracketgenerator.generatebracket(tournament)
    
    def roundsplayed(self, teams):
        """Return how many rounds can be played and how many extra matches are needed based on team count"""
        return self.__bracketgenerator.playingames(teams)
    
    def getMatchbyID(self, id: str):
        """Get a match by its ID"""
        return self.__matchlogic.getMatchbyID(id)
      
    def updateMatchWinner(self, match, team):
        """Updates and saved the match winner"""
        self.__matchlogic.updateMatch(match, team, 'updatewinner')

    
    def availableteams(self, tournament : Tournament):
        """Returns a list of teams that are not already registered to the tournament"""
        return self.__Tournamentmanager.availableteams(tournament)
      
    def saveBracket(self, bracket):
        """Save bracket to file"""
        self.__Tournamentmanager.saveBracket(bracket)

    def saveTeam(self, team: Team):
        """Save team to file"""
        self.__Teamlogic.saveTeam(team)
    
    def updateBracket(self, tournament):
        """Update tournament bracket and save all tournament data"""
        self.__bracketgenerator.updatebracket(tournament)
        self.__Tournamentmanager.updateTournament(tournament,None ,'updateall')
    
    def updateOrMatches(self, tournament: Tournament, matchwinner: str):
        """Puts the winning team in the A or B placeholder teams"""
        self.__bracketgenerator.updateOrMatches(tournament, matchwinner)
        return


    def returnMatchWinner(self, match, scores):
        """Returns a winner of a match based on the score"""
        return self.__matchlogic.returnMatchWinnerconfirmation(match, scores)
    
    def confirmMatchWinner(self, tournament: Tournament, match: Match, scores)-> tuple[str,str]:
        """Input scores is a list [1,2] score 1(index 0) is team_A score and score 2(index 1) is team_B score
        To update the bracket correctly use these commands in this order \n
        \n
        1. matchloser, matchwinner = llapi.confirmMatchWinner(match, score) \n
        2. llapi.removeTeamfromTournament(tournament, matchloser) \n
        3. llapi.updateOrMatches(tournament,matchwinner) \n
        4. llapi.updateBracket(tournament)
        """
        matchloser, matchwinner = self.__matchlogic.confirmMatchWinner(match, scores)
        self.removeTeamfromTournament(tournament, matchloser)
        self.updateOrMatches(tournament, matchwinner)
        winnerteam = self.getTeambyName(matchwinner, tournament)
        loserteam = self.getTeambyName(matchloser, tournament)
        self.__Teamlogic.updateTeam(None,'updatewins',winnerteam)
        self.__Teamlogic.updateTeam(None,'updatelosses',loserteam)
        self.updateBracket(tournament)
        return
        
    def populateBracket(self, bracket):
        """Replace match IDs in bracket with loaded match objects"""
        self.__Tournamentmanager.populateBracket(bracket)

    def removeTeamfromTournament(self, tournament: Tournament, teamname: str):
        """Removes team from tournament, input teamname. Meant to be used after updating matches with confirmMatchWinner in logic api"""
        self.__Tournamentmanager.removeTeamfromTournament(tournament, teamname)
        return
    def getNamedRounds(self, bracket):
        return self.__bracketlogic.getnamedrounds(bracket)
    
    def reloadTournament(self, tournament: Tournament):
        return self.__Tournamentmanager.reloadTournament(tournament)
    
    def getTeambyName(self, teamname, tournament: Tournament):
        return self.__Teamlogic.get_team_by_teamname(teamname, tournament)
###############testing area#############

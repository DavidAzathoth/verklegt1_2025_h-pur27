from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Bracket import Bracket
from Models.Match import Match
from LogicLayer.TeamLogic import Teamlogic
from LogicLayer.MatchLogic import MatchLogic
from datetime import datetime, date

class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__logichandler = logicHandler()
        self.__tournamentmodel = Tournament
        self.__bracketmodel = Bracket
        self.__matchmodel = Match
        self.__teamlogic = Teamlogic(self.__dataApi)
        self.__matchlogic = MatchLogic(self.__dataApi)
        
        

    def createTournament(self, tournament: list):
        return self.__logichandler.createModel(self.__tournamentmodel,tournament)


    def getTournaments(self):
        """Returns a list of loaded Tournament models"""
        raw_list = self.__dataApi.loadTournaments()
        tournamentlist: list[Tournament] = self.__logichandler.loadmodels(self.__tournamentmodel, raw_list)
        return tournamentlist
    
    def getTournamentbyName(self, name: str, tournamentlist: list[Tournament]):
        """Returns the tournament model that the given name belongs to, must provide a list of already loaded tournament models"""
        for tournament in tournamentlist:
            if name.lower().strip() == tournament.name.lower().strip():
                return tournament
        return None
            
    def populateTournament(self, tournament: Tournament):
        """Populates the given tournament, loads the loaded Bracket model with loaded Match models into the tournament.
        This also ensures that all Team models are loaded into the tournament"""
        if type(tournament.teams) == list:
            if len(tournament.teams) > 0:
                if type(tournament.teams[0]) == Team:
                    return False
        teams = self.__teamlogic.getTeams()
        teamobjects=list(map(lambda team: self.__teamlogic.get_team_by_teamID(team, teams), (tournament.teams)))
        bracket = self.getBracketByTournament(tournament)
        tournament.bracket = bracket
        tournament.teams = teamobjects
        playingteams=list(map(lambda playingteam: self.__teamlogic.get_team_by_teamID(playingteam, teamobjects), (tournament.playingteams)))
        tournament.playingteams = playingteams
        if None in tournament.teams:
            tournament.teams.remove(None)
        if None in tournament.playingteams:
            tournament.playingteams.remove(None)
        if tournament.bracket == None:
            tournament.bracket=''
        return tournament
    
    def unpopulateTournament(self, tournament: Tournament):
        """Unpopulates the tournament, unpacks all loaded models inside the tournament. This is used before saving"""
        if type(tournament.teams) == list:
            if '' not in tournament.teams:
                if len(tournament.teams) > 0:
                    teamids = [x.teamID for x in tournament.teams]
                    tournament.teams = teamids

        if type(tournament.playingteams) == list:
            if '' not in tournament.playingteams:
                if len(tournament.playingteams) > 0:
                    playingteamids = [x.teamID for x in tournament.playingteams]
                    tournament.playingteams = playingteamids
        return tournament
            
    
        
    def saveTournament(self,tournament: Tournament):
        """Adds the tournament to file"""
        self.unpopulateTournament(tournament)
        self.__dataApi.saveTournament(tournament.createCSVDict())
        return
    
    def updateTournament(self, tournament: Tournament, input: object = None, operation: str = None ):
        """Updates the given tournament or adds team. operations are 'addteam' or 'updateall'. Update all also updates all loaded models in the
        tournament and overwrites everything in file that has the same id or name. addteam will simply add a team to the tournament and update the file."""
        if tournament.active==False:
            return False
        tournaments = self.getTournaments()
        for t in tournaments:
            if tournament.name == t.name:
                index = tournaments.index(t)
                break
        tournaments.remove(t)
        if '' in tournament.teams: #Cleans up empty string that appears when list is first created
            tournament.teams.pop(0)
        if '' in tournament.matchesList:
            tournament.matchesList.pop(0)
        if '' in tournament.matchHistory:
            tournament.matchHistory.pop(0)


        if operation == 'addteam':
            if self.checkDuplTeams(tournament, input) == False:
                return False
            if self.validateTournamentBracket(tournament) == True:
                return False
            tournament.teams.append(input)
        if operation == 'updateall':
            if type(tournament.bracket) == Bracket:
                self.updateBracket(tournament.bracket)
            for team in tournament.teams:
                self.__teamlogic.updateTeam(None,None,team)

        self.unpopulateTournament(tournament)
        tournaments.insert(index, tournament)
        tournaments=[t.createCSVDict() for t in tournaments]
        self.__dataApi.updateTournaments(tournaments)
        self.populateTournament(tournament)
        return True

    def addTeamtoTournament(self, tournament: Tournament, team: Team):
        if self.checkDuplTeams(tournament, team):
            tournament.teams.append(team)

    def removeTeamfromTournament(self, tournament: Tournament, teamname: str):
        """Removes team from tournament, input teamname. Meant to be used after updating matches with confirmMatchWinner in logic api"""
        for team in tournament.playingteams:
            if team.teamName==teamname:
                tournament.playingteams.remove(team)

    def checkDuplTeams(self, tournament: Tournament, team: Team):
        reg_team : Team
        for reg_team in tournament.teams:
            if reg_team.teamID == team.teamID:
                return False
        return True
    
    def getBrackets(self)->list[Bracket]:
        raw_list = self.__dataApi.loadBrackets()
        bracketlist: list[Bracket] = self.__logichandler.loadmodels(self.__bracketmodel, raw_list)
        for bracket in bracketlist:
            bracket.rounds=eval(bracket.rounds)
        return bracketlist
    
    def getBracketByTournament(self,tournament: Tournament):
        bracketlist = self.getBrackets()
        bracket: Bracket
        for bracket in bracketlist:
            if bracket.tournamentname==tournament.name:
                self.populateBracket(bracket)
                return bracket
        return
            

    def saveBracket(self, bracket: Bracket):
        """Adds a new bracket to file"""
        bracket=self.unpopulateBracket(bracket)
        self.__dataApi.saveBracket(bracket.createCSVDict())


    def populateBracket(self, bracket: Bracket):
        """Populates the given bracket will all match models that belong to it"""
        rounds: dict[list]
        for round in bracket.rounds.keys():
            roundobjects = list(map(self.__matchlogic.getMatchbyID, bracket.rounds.get(round)))
            bracket.rounds[round]=roundobjects
        return bracket
    


    def availableteams(self, tournament : Tournament) -> list[Team]:
        all_teams: list[Team] = self.__teamlogic.getTeams()
        tournament_teams: list[Team] = tournament.teams
        if None in tournament_teams:
            tournament_teams.pop(0)
        teamIDs = []
        for team in tournament_teams:
            tID = team.teamID.strip()
            if tID != "":
                teamIDs.append(tID)
        available = []
        for team in all_teams:
            if team.teamID.strip() not in teamIDs:
                available.append(team)    
        return available



    def unpopulateBracket(self, bracket: Bracket):
        """Unpacks the Match models in the bracket"""
        for round in bracket.rounds.keys():
            matchids=[match.matchID for match in bracket.rounds.get(round)]
            bracket.rounds[round] = matchids
        return bracket
    
    def updateBracket(self, bracket: Bracket):
        """Updates all matches in the bracket"""
        for round in bracket.rounds.keys():
            match: Match
            for match in bracket.rounds.get(round):
                self.__matchlogic.updateMatch(match)
    
    def reloadTournament(self, tournament: Tournament):
        """This updates the entire tournament, bracket, matches, teams and all. Then gets a new tournament from file with the same name (itself) and deletes the loaded tournament. 
        This is used to ensure the tournament updates correctly"""
        self.updateTournament(tournament,None,'updateall')
        tournamentlist = self.getTournaments()
        reloaded_tournament = self.getTournamentbyName(tournament.name,tournamentlist)
        self.populateTournament(reloaded_tournament)
        del(tournament)
        return reloaded_tournament
    
    def geteligibleMatches(self, tournament: Tournament):
        """Returns matches that can be updated"""
        updateable_matches = []
        match: Match
        for round in tournament.bracket.rounds.keys():
            for match in tournament.bracket.rounds.get(round):
                if match.team_A == 'TBD' or match.team_B == 'TBD':
                    break
                if len(match.team_A.split(' or ')) < 2 and len(match.team_B.split(' or ')) < 2 and (match.matchPlayed=='False' or match.matchPlayed==False):
                    updateable_matches.append(match)
        return updateable_matches
    
    def getcompleteMatches(self, tournament: Tournament):
        """Returns all completed matches in the tournament"""
        complete_matches = []
        for round in tournament.bracket.rounds.keys():
            for match in tournament.bracket.rounds.get(round):
                if match.matchPlayed == 'True' or match.matchPlayed == True:
                    complete_matches.append(match)
        return complete_matches
    
    def validate_start_end_date(self, startdate, enddate):
        """validate start and enddate for tournament"""
        startdate = datetime.strptime(startdate, "%Y-%m-%d")
                
        enddate = datetime.strptime(enddate, "%Y-%m-%d")

        if enddate <= startdate:
            return None

        return startdate, enddate
    def validateTournamentBracket(self, tournament: Tournament)-> bool:
        """Returns False if the tournament has a bracket, otherwise True"""
        if type(tournament.bracket) is not Bracket:
            return False
        else:
            return True


from StorageLayer.storageApi import DataAPI
from LogicLayer.logicHandler import logicHandler
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Bracket import Bracket
from Models.Match import Match
from LogicLayer.TeamLogic import Teamlogic
from LogicLayer.MatchLogic import MatchLogic
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
        raw_list = self.__dataApi.loadTournaments()
        tournamentlist: list[Tournament] = self.__logichandler.loadmodels(self.__tournamentmodel, raw_list)
        return tournamentlist
    
    def getTournamentbyName(self, name: str, tournamentlist: list[Tournament]):
        for tournament in tournamentlist:
            if name.lower().strip() == tournament.name.lower().strip():
                return tournament
            
    def populateTournament(self, tournament: Tournament):
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
        if type(tournament.teams) == list:
            if len(tournament.teams) > 0:
                teamids = [x.teamID for x in tournament.teams]
                tournament.teams = teamids
        if type(tournament.playingteams) == list:
            if len(tournament.playingteams) > 0:
                playingteamids = [x.teamID for x in tournament.playingteams]
                tournament.playingteams = playingteamids
        return tournament
    
    
        
    def saveTournament(self,tournament: Tournament):
        self.unpopulateTournament(tournament)
        self.__dataApi.saveTournament(tournament.createCSVDict())
        return
    
    def updateTournament(self, tournament: Tournament, input: object = None, operation: str = None ):
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
        bracket=self.unpopulateBracket(bracket)
        self.__dataApi.saveBracket(bracket.createCSVDict())


    def populateBracket(self, bracket: Bracket):
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
        for round in bracket.rounds.keys():
            matchids=[match.matchID for match in bracket.rounds.get(round)]
            bracket.rounds[round] = matchids
        return bracket
    
    def updateBracket(self, bracket: Bracket):
        for round in bracket.rounds.keys():
            match: Match
            for match in bracket.rounds.get(round):
                self.__matchlogic.updateMatch(match)
    
    def reloadTournament(self, tournament: Tournament):
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

    def returnRoundNames(self, tournament: Tournament):
        roundlist=['First rounds','Second rounds','Third rounds','Fourth rounds','Fifth rounds','Sixth rounds','Seventh rounds','Eight rounds','Ninth rounds','Tenth rounds']
        finallist=['Quarter-finals','Semi-finals','Finals']
        roundnames=[]
        totalrounds=len(tournament.bracket.rounds)
        for i in range(1,totalrounds-2):
            roundnames.append(roundlist.pop(0))
        roundnames+=finallist
        return roundnames

        



#def populateTournament(self, tournament: Tournament):
#        teams = self.__teamlogic.getTeams()
#        teamobjects=list(map(lambda team: self.__teamlogic.get_team_by_teamID(team, teams), (tournament.teams)))
#        tournament.teams=teamobjects
#        return tournament


#    def calculaterounds(self, teams: list[Team]):
#        oddrounds = 0
#        totalrounds = 0
#        divbytwo = len(teams)
#        while divbytwo != 1:
#            temp=divbytwo / 2
#            if divbytwo / 2 != 0:
#                oddrounds += 1
#                divbytwo=divbytwo-1

#            
        


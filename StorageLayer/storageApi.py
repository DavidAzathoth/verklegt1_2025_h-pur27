from StorageLayer.storageHandler import StorageHandler
from StorageLayer.TournamentData import TournamentData
from StorageLayer.TeamData import TeamData
from StorageLayer.CaptainData import CaptainData
from StorageLayer.PlayerData import PlayerData
from StorageLayer.MatchData import MatchData
from Models.Team import Team

class DataAPI:
    def __init__(self):
        self.__storagehandler=StorageHandler()
        self.__tournamentData=TournamentData(self.__storagehandler)
        self.__teamData=TeamData(self.__storagehandler)
        self.__captainData=CaptainData(self.__storagehandler)
        self.__playerData=PlayerData(self.__storagehandler)
        self.__matchData=MatchData(self.__storagehandler)
    def loadTeams(self):
        return self.__teamData.load_teams()
    
    def saveTeam(self,data):
        self.__teamData.save_team(data)
        return
    
    def loadTournaments(self):
        return self.__tournamentData.load_tournaments()

    def saveTournament(self,data):
        self.__tournamentData.save_tournament(data)
        return
    def loadCaptains(self):
        return self.__captainData.load_captains()
    
    def updateCaptains(self,data):
        self.__captainData.update_captains(data)
        return
    
    def loadPlayers(self):
        return self.__playerData.load_players()
    
    def savePlayer(self,data):
        self.__playerData.savePlayer(data)
        return
    
    def loadMatches(self):
        return self.__matchData.load_matches()
    
    def saveMatch(self, data):
        self.__matchData.save_match(data)
        return

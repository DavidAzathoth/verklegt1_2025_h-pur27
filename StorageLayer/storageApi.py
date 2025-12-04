from StorageLayer.storageHandler import StorageHandler
from StorageLayer.TournamentData import TournamentData
from StorageLayer.TeamData import TeamData
from StorageLayer.CaptainData import CaptainData
from Models.Team import Team

class DataAPI:
    def __init__(self):
        self.__storagehandler=StorageHandler()
        self.__tournamentData=TournamentData(self.__storagehandler)
        self.__teamData=TeamData(self.__storagehandler)
        self.__captainData=CaptainData(self.__storagehandler)
    def loadTeams(self):
        return self.__teamData.load_teams()
    def saveTeam(self,data):
        self.__teamData.save_team(data)
        return
    def loadTournaments(self):
        return self.__tournamentData.load_tournament()

    def saveTournament(self,data):
        self.__tournamentData.save_tournament(data)
        return
    def loadCaptains(self):
        return self.__captainData.load_captains()
    
    def updateCaptains(self,data):
        self.__captainData.update_captains(data)
        return

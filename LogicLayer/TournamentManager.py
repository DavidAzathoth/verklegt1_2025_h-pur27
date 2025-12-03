from StorageLayer.storageApi import DataAPI
from Models.Tournament import Tournament
class Tournamentmanager:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass

    def createTournament(self, tournament):
        Venue = tournament[0]
        name = tournament[1]
        startDate = tournament[2]
        endDate = tournament[3]
        contactEmail = tournament[4]
        contactPhone = tournament[5]
        tournament = Tournament(Venue, name, startDate, endDate, contactEmail, contactPhone)
        return tournament


    def getTournament(self):
        return self.__dataApi.loadTournament()


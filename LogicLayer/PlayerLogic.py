from StorageLayer.storageApi import DataAPI
from Models.Player import Player

class Playerlogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass

    def createplayer(self, player: list):
        teamID = player[0]
        playerGamertag = player[1]
        fullname = player[2]
        phoneNumber = player[3]
        emailAddress = player[4]
        address = player[5]
        link = player[6]
        dateOfBirth = player[7]
        self.__dataApi.savePlayer()
        return
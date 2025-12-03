from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI
from StorageLayer.storageHandler import StorageHandler
from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from Models.Player import Player
from StorageLayer.storageApi import DataAPI
from Models.ViewTeamsMenu import ShowTeams



listi = input()
minnlisti = listi.split()
LogicAPI.createtournament(minnlisti)

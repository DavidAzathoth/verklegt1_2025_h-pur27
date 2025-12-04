from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI
from StorageLayer.storageHandler import StorageHandler
from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from Models.Player import Player
from StorageLayer.storageApi import DataAPI
from Models.ViewTeamsMenu import ShowTeams

da = DataAPI()
logic = LogicAPI()
tournaments = logic.gettournament()
#print(tournaments)
#teams = logic.showTeams()
#print(teams)
MenuUI(logic).show_main_menu()

#listi = input("tournament info")
#minnlisti = listi.split()
#LogicAPI.createTournament(minnlisti)

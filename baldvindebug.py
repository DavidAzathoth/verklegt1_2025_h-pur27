
# da=DataAPI()
# dd=LogicAPI()
# teammenu=ShowTeams(dd.createTeamsString())
# teammenu.page+=1
# print(teammenu)
# print(dd.createTeamsString())
from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI
from StorageLayer.storageHandler import StorageHandler
from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from Models.Player import Player
from StorageLayer.storageApi import DataAPI
from Models.ViewTeamsMenu import ShowTeams

# required_inputs=['venue: ','name: ','startdate: ','enddate: ','contactemail: ','contactperson: ']
# for inputs in required_inputs:
#     add=input(f'{inputs}')
#     inputlisti.append(add)

# t2=llapi.createtournament(inputlisti)

print(MenuUI(LogicAPI()).show_main_menu())

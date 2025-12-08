
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
from UiLayer.UIMain import UIMain
from LogicLayer.menuLogic import MenuLogic
from datetime import datetime

"""Main loop test"""
# run = UIMain()

# run.mainloop()


"""Test for Email verification"""
# data_api = DataAPI()
# menu_logic = MenuLogic(data_api)
# run: tuple = menu_logic.emailverification(input("Email: "))

# if run[1] == True:
#     print(run[0])
# else:
#     while run[1] == False:
#         print(run[0])
#         run = menu_logic.emailverification(input("Email: "))


# if (LogicAPI().getCaptain("FalleN")):
#     print('Captain exists!')


# MenuUI(LogicAPI()).show_team_creation_menu("baldvin")


while True:
    try:
        dob = datetime.strptime(input("Date of birth (YYYY-MM-DD): "), "%Y-%m-%d")
        break
    except ValueError:
        print("ERROR: Invalid input. Please enter a valid date")

print(dob.date())
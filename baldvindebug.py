
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
run = UIMain()

run.mainloop()



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


# while True:
#     try:
#         dob = datetime.strptime(input("Date of birth (YYYY-MM-DD): "), "%Y-%m-%d")
#         break
#     except ValueError:
#         print("ERROR: Invalid input. Please enter a valid date")

# print(dob.date())

"""captain"""
# Sheriff_Norris
# Chuck Norris
# 1940-03-10
# 123 chucknorrisstreet
# 123456789
# gmail@chucknorris.com
# https://www.instagram.com/chucknorris/?hl=en

"""player1"""
# Disciple1
# Bob
# 2002-12-12
# 234 somewhere
# 3459621
# bob@gmail.com


"""player2"""
# Disciple2
# Jim
# 2001-11-11
# 3452 whatever
# 1897253
# jim@gmail.com

"""player3"""
# Disciple3
# Josh
# 2000-12-12
# 432 somestreet
# 423895
# josh@gmail.com

"""player4"""
# Disciple4
# Gary
# 2003-02-02
# 246 street
# 2175219
# gary@gmail.com


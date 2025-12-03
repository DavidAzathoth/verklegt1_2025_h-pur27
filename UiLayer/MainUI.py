from LogicLayer.logicAPI import LogicAPI
#from AllMenuUI import menuUI


class MainMenuUI:
    #def __init__(self, menuUI):
    def __init__(self):
        pass
        self.llapi=LogicAPI()
        """## UI strings ##
        main_menu - The main menu of the program\n
        public_menu - Public user interface\n
        organizer_menu - Shows organizer interface after login\n
        captain_menu - Shows team captain interface after login\n
        logic_auth - authenticates login (connected to logic layer)"""
    
    # snake case used for this function to keep UI elements in the same style.
    def testfunction(self): #<--- delete this at latest convenience 
        pass

#     def captain_menu(self):
#         """prints captain_menu, needs captainID to be declared for MainMenu class before calling, otherwise None will be printed as Team Captain"""
#         return(f"""
# ---------------------------
#  RU's e-Sport Extravaganza
# ---------------------------
# {self.captain_handle}

# You have no current team

# 1. Create team
# 2. Back
# """)


# Testing zone vv
#menu = MainMenu()
##
#
#menu.captain_handle = "Sheriff Norris"
#print(menu.captain_menu())

# calls logic for findteam, which calls data to retrieve all teams, then logic will find team name and send it here.


# Testing opening files, don't leave this in here


##Finding team and printing team name and roster
# IOapi=StorageManager()
# teams=IOapi.loadTeams()
# for team in teams:
#    if team.get('teamName')=='PARIVISION':
#        foundteam=team.get('teamName')
#        players=team.get('roster').split(',')
#
# print(f"""
# {'-'*len(foundteam)}
# {foundteam}
# {'-'*len(foundteam)}
# """)
# for player in players:
#    print(player)

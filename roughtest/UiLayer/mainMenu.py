from roughtest.LogicLayer.LogicHandler import LogicAPI

class MainMenu:
    def __init__(self):
        """## UI strings ##
            main_menu - The main menu of the program\n
            public_menu - Public user interface\n
            organizer_menu - Organizer menu\n
            captain_menu - Team captain menu"""
        self.captain_handle=None
        self.main_menu=f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Main Menu

1. Public
2. Organizer
3. Team captain
0. Quit
"""
        self.public_menu=f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Public menu

1. View tournaments
2. View teams/players
3. Back
"""
        self.organizer_menu=f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Organizer Menu

1. Create tournament
2. Add teams to tournament
3. Generate schedule
4. Update results
5. Back
"""
    #snake case used for this function to keep UI elements in the same style.
    def captain_menu(self):
        """prints captain_menu, needs captainID to be declared for MainMenu class before calling, otherwise None will be printed as Team Captain"""
        return(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{self.captain_handle}

You have no current team

1. Create team
2. Back
""")




#Testing zone vv
menu=MainMenu()


menu.captain_handle=("Sheriff Norris")
print(menu.captain_menu())

llapi=LogicAPI()
#calls logic for findteam, which calls data to retrieve all teams, then logic will find team name and send it here. 
print(llapi.findteam('fnatic'))


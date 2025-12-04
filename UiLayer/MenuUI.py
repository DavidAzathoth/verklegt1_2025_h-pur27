from LogicLayer.logicAPI import LogicAPI

class MenuUI:
    def __init__(self, logic_api: LogicAPI):
        self.__logic_api = logic_api

    def __prompt_options(self, valid_options: list[str]):
        valid_lower = [i.lower() for i in valid_options]

        while True:
            choice = input("> ").strip().lower()

            if choice in valid_lower:
                return choice

            print(f"Invalid input. Valid options are: {'. '.join(valid_lower)}")


    def show_main_menu(self):
        """Prints out the main menu
        returns: "TOURNAMENTS", "TEAMS", "ORGANIZER", "TEAM CAPTAIN", "QUIT" """
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Main Menu

1. Tournaments
2. Teams
3. Organizer
4. Team Captain

q. Quit"""
        )

        choice = self.__prompt_options(["1", "2", "3", "4", "q"])

        if choice == "1":
            return "TOURNAMENTS"
        if choice == "2":
            #Testing purposes#
            teams=self.__logic_api.showTeams()
            while True:
                print(teams)
                next=input('Press enter to see next page')
                teams.endpage+=5
                teams.startpage+=5
            #Testing purposes#
            return "TEAMS"
        if choice == "3":
            return "ORGANIZER"
        if choice == "4":
            captain_handle: str = input("Handle: ")
            team = self.__logic_api.get_team_by_captain(captain_handle)
            if team is None:
                self.show_captain_no_team_menu(captain_handle)
                return "DOES NOT HAVE TEAM"
            else:
                self.show_captain_has_team_menu(captain_handle)
                return "HAS TEAM"
        return "QUIT"


    def show_tournaments_menu(self):
        """Prints list of tournaments
        returns: # TODO """
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
List of tournaments""") 
        pass
    

    def show_teams_menu(self):
        """Prints teams menu
        returns: "PRINT LIST OF TEAMS", "SEARCH FOR A TEAM" """

        print("""
---------------------------
 RU's e-sport extravaganza 
---------------------------
Teams menu

1. Print list of teams
2. Search for team

b. Back
h. Home
q. Quit""")
        
        choice = self.__prompt_options(["1", "2", "b", "h", "q"])

        if choice == "1":
            return "PRINT LIST OF TEAMS"
        if choice == "2":
            return "SEARCH FOR A TEAM"
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"


    def show_organizer_menu(self):
        """Print organizer menu.
        returns: "CREATE TOURNAMENT", "ADD TEAMS TO TOURNAMENT, "GENERATE SCHEDULE", "UPDATE RESULTS", "BACK", "HOME", "QUIT" """
        
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Organizer Menu

1. Create tournament
2. Add teams to tournament
3. Generate schedule
4. Update results

b. Back
h. Home
q. Quit""")
        
        choice = self.__prompt_options(["1", "2", "3", "4", "b", "h", "q"])

        if choice == "1":
            return "CREATE TOURNAMENT"
        if choice == "2":
            return "ADD TEAMS TO TOURNAMENT"
        if choice == "3":
            return "GENERATE SCHEDULE"
        if choice == "4":
            return "UPDATE RESULTS"
        if choice == "b":
            return "BACK"
        return "QUIT"


    def show_captain_no_team_menu(self, captain_handle: str):
        """Prints out captains menu if no team
        returns: "CREATE TEAM", "BACK", "HOME", "QUIT" """
        
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{captain_handle} Menu

You have no current team

1. Create team

b. Back
h. Home
q. Quit""")
        
        choice = self.__prompt_options(["1", "b", "h", "q"])

        if choice == "1":
            return "CREATE TEAM"
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"


    def show_captain_has_team_menu(self, captain_handle: str):
        """Prints out captain menu if has team"""

        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{captain_handle} Menu

1. View my team/players
2. Edit team information

b. Back
h. Home
q. Quit""")
        
        choice = self.__prompt_options(["1", "2", "b", "h", "q"])
        if choice == "1":
            return "VIEW MY TEAM/PLAYERS"
        if choice == "2":
            return "EDIT TEAM INFORMATION"
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"
    
    def show_tournament_creation_menu(self):
        """Shows the tournament creation menu"""
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Tournament creation menu""")
        self.__logic_api.createtournament([input("Venue: "), input("Name: "), input("StartDate: "), input("EndDate: "), input("ContactEmail: "), input("ContactPhone: ")])
        
        print("-----------------------------")
        print("Tournament has been created!")
        print("""
b. Back
h. Home
q. Quit""")
        
        choice = self.__prompt_options(["b", "h", "q"])
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"
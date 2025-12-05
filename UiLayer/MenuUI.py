from LogicLayer.logicAPI import LogicAPI
from UiLayer.ViewTeamsMenu import ShowTeams

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
        
#========= MAIN MENU INTERFACE ==========
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Main Menu

1. Tournaments
2. Teams
3. Organizer
4. Team Captain

q. Quit
""")
#========================================

        choice = self.__prompt_options(["1", "2", "3", "4", "q"])

        if choice == "1":
            return "TOURNAMENTS"
        if choice == "2":
            return "TEAMS"
        if choice == "3":
            return "ORGANIZER"
        if choice == "4":
            captain_handle: str = input("Handle: ")
            team = self.__logic_api.get_team_by_captain(captain_handle)
            if team is None:
                return ("CAPTAIN HAS NO TEAM", captain_handle)
            else:
                return ("CAPTAIN HAS TEAM", captain_handle)
        return "QUIT"


    def show_tournaments_menu(self):
        #TODO GET TOURNAMENTS
        """Prints list of tournaments
        returns: # TODO """
        
#------LIST OF TOURNAMENTS INTERFACE---------------
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
List of tournaments
""") 
        pass
    

    def show_teams_menu(self):
        """Prints teams menu
        returns: "PRINT LIST OF TEAMS", "SEARCH FOR A TEAM", "BACK", "QUIT" """

#========= TEAMS MENU INTERFACE ========
        print("""
---------------------------
 RU's e-sport Extravaganza 
---------------------------
Teams menu

1. Print list of teams
2. Search for team

b. Back
q. Quit
""")
#=======================================
 
        choice = self.__prompt_options(["1", "2", "b", "q"])

        if choice == "1":
            return "PRINT LIST OF TEAMS"
        if choice == "2":
            team = input("Team name: ").strip().lower()
            return "SEARCH FOR A TEAM"
        if choice == "b":
            return "BACK"
        return "QUIT"


    def show_organizer_menu(self):
        """Print organizer menu.
        returns: "CREATE TOURNAMENT", "ADD TEAMS TO TOURNAMENT, "GENERATE SCHEDULE", "UPDATE RESULTS", "BACK", "QUIT" """
        
#========ORGANIZER MENU INTERFACE ========
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
q. Quit""")
#=========================================
        
        choice = self.__prompt_options(["1", "2", "3", "4", "b", "q"])

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
        """Prints out captains menu if he has no team
        returns: "CREATE TEAM", "BACK", "QUIT" """

#========= CAPTAIN NO TEAM INTERFACE ===========     
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{captain_handle} Menu

You have no current team

1. Create team

b. Back
q. Quit""")
#===============================================
        
        choice = self.__prompt_options(["1", "b", "q"])

        if choice == "1":
            return "CREATE TEAM"
        if choice == "b":
            return "BACK"
        return "QUIT"


    def show_captain_has_team_menu(self, captain_handle: str):
        """Prints out captain menu if has team"""

#========= CAPTAIN HAS TEAM MENU INTERFACE =========
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{captain_handle} Menu

1. View my team/players
2. Edit team information

b. Back
q. Quit
""")
#===================================================
        
        choice = self.__prompt_options(["1", "2", "b", "q"])
        if choice == "1":
            return "VIEW MY TEAM/PLAYERS"
        if choice == "2":
            return "EDIT TEAM INFORMATION"
        if choice == "b":
            return "BACK"
        return "QUIT"
    

    def show_tournament_creation_menu(self):
        """Shows the tournament creation menu"""

#=========== TOURNAMENT CREATION MENU INTERFACE ============
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Tournament creation menu
""")
#===========================================================
        
        # Asks to input informattion to create tournament
        self.__logic_api.createtournament([input("Venue: "), input("Name: "), input("StartDate: "), input("EndDate: "), input("ContactEmail: "), input("ContactPhone: ")])

#=============== TOURNAMENT HAS BEEN CREATED ==============
        print("""
              
-----------------------------
Tournament has been created!
              
b. Back
h. Home
q. Quit
""")
#==========================================================
        
        choice = self.__prompt_options(["b", "h", "q"])
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"
    

    def show_team_creation_menu(self, captain_handle):
        """Prints out team creation menu where team information is given.
        returns: "ADD PLAYERS TO TEAM" or "CANCEL" """

#============ TEAM CREATION MENU INTERFACE =============
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Team creation menu
Team captain: {captain_handle}
""")
#=======================================================
        totalTeams = self.__logic_api.getTeams()
        newTeam = self.__logic_api.createteam([])


    def show_view_teams_menu(self):
        """shows list of 5 teams at a time. allows to view team info.
        returns: "TEAM INFO", "BACK", "QUIT" """
        
        teams = self.__logic_api.getTeams()

        team_names: list = [t.teamName for t in teams]

        viewer = ShowTeams(team_names)
        
        # loop to view 5 teams at a time
        while True:

#=============== View teams menu interface ===============
            print(viewer)
            print("""             
ENTER. Next Page
1-5. View team details
b. Back
q. Quit
""")
#=========================================================

            choice = self.__prompt_options(["1", "2", "3", "4", "5", "", "b", "q"])

            #select team by number
            if choice.isdigit():
                number = int(choice)
                team_name = viewer.get_team_by_number(number)
                
                #find team object
                for t in teams:
                    if t.teamName == team_name:
                        return ("TEAM INFO", t)
                continue

            if choice == "":
                viewer.next_page()
                continue

            if choice == "b":
                return "BACK"
            
            return "QUIT"
        

    def show_team_info(self, team):
        """Shows team information for selected team
        returns: "BACK", "HOME", "QUIT" """

        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
View {team.teamName} information

Name: {team.teamName}
Captain: {team.captainHandle}
Player handles:""")
        for p in team.roster:
            print(f"- {p}")
        
        print(f"""
Wins: {team.wins}
Losses: {team.losses}

b. Back
h. Home
q. Quit
""")

        choice = self.__prompt_options(["b", "h", "q"])

        if choice == "b":
            return "BACK"
        
        if choice == "h":
            return "HOME"
        
        return "QUIT"
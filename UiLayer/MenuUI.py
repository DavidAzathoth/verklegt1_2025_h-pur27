from LogicLayer.logicAPI import LogicAPI
from UiLayer.selectfrompage import SelectFromPage
from datetime import datetime
from Models.Team import Team

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


    def set_start_end_date(self):
        while True:
            try:
                startdate = datetime(
                    int(input("Start date year: ")),
                    int(input("Start date month: ")),
                    int(input("Start date day: "))
                    )
                
                enddate = datetime(
                    int(input("End date year: ")),
                    int(input("End date month: ")),
                    int(input("End date day: "))
                    )
                
            except ValueError:
                print("please enter valid numbers for year, month, day")
                continue

            if enddate < startdate:
                print("ERROR: End date must be after start date")
                continue

            print(f"Startdate: {startdate.date()} \nEnd date: {enddate.date()}")

            return startdate, enddate


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
        """Prints list of tournaments
        returns: ("TOURNAMENT INFO",  tournament: object), "BACK", "QUIT"  """
        
        tournaments = self.__logic_api.gettournament()

        tournament_names: list[str] = [t.name for t in tournaments]

        viewer = SelectFromPage(tournament_names)

        #loop to view tournaments 5 at a time
        while True:

#------LIST OF TOURNAMENTS INTERFACE---------------
            print(f"""
---------------------------
RU's e-Sport Extravaganza
---------------------------
List of tournaments
              
{viewer.currentPage()}
              
ENTER. Next page
1-5. View tournament details
b. Back
q. Quit              
""") 
            choice = self.__prompt_options(["1", "2", "3", "4", "5", "", "b", "q"])

            #select tournament by number
            if choice.isdigit():
                num = int(choice)
                tournament_name = viewer.select_item_by_number(num)
                
                # find tournament object
                for t in tournaments:
                    if t.name == tournament_name:
                        return ("TOURNAMENT INFO", t)
                continue
            
            #press ENTER to go to next page
            if choice ==  "":
                viewer.next_page()
                continue

            if choice == "b":
                return "BACK"
            
            return "QUIT"
        

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
              
Please enter tournament details:
""")  
        venue: str = input("Venue: ").strip()
        name: str = input("Name: ").strip()
        startdate, enddate = self.set_start_end_date()
        check_contact_email: tuple = self.__logic_api.emailVerification(input("ContactEmail: "))
        while check_contact_email[1] == False:
            print(check_contact_email[0])
            check_contact_email: tuple = self.__logic_api.emailVerification(input("ContactEmail: "))
        contactemail = check_contact_email[0]
        contactphone = int(input("ContactPhone: "))

#===========================================================

        # Asks to input informattion to create tournament
        tournament = self.__logic_api.createtournament([venue, name, startdate.date(), enddate.date(), contactemail, contactphone ])

        #self.__logic_api.saveTournament(tournament) <--- saves tournament
        print("""

1. Confirm creation
c. Cancel
""")
        choice = self.__prompt_options(["1", "c"])
        if choice == "c":
            return "BACK"
        if choice == "1":
            self.__logic_api.saveTournament(tournament)

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
    

    def show_team_creation_menu(self, captain_handle: str):
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
        newPlayer = self.__logic_api.createPlayer([])
        self.__logic_api.savePlayer(newPlayer)
        # TODO CREATE TEAM AND PLAYER MENU


    def show_view_teams_menu(self):
        """shows list of 5 teams at a time. allows to view team info.
        returns: "TEAM INFO", "BACK", "QUIT" """
        
        teams = self.__logic_api.getTeams()

        team_names: list = [t.teamName for t in teams]

        viewer = SelectFromPage(team_names)
        
        # loop to view 5 teams at a time
        while True:

#=============== View teams menu interface ===============
            print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
View teams menu
              
{viewer.currentPage()}

ENTER. Next page
1-5. View team details
b. Back
q. Quit
""")
#=========================================================

            choice = self.__prompt_options(["1", "2", "3", "4", "5", "", "b", "q"])

            #select team by number
            if choice.isdigit():
                number = int(choice)
                team_name = viewer.select_item_by_number(number)
                
                #find team object
                for t in teams:
                    if t.teamName == team_name:
                        return ("TEAM INFO", t)
                continue
            
            #press ENTER to go to next page
            if choice == "":
                viewer.next_page()
                continue

            if choice == "b":
                return "BACK"
            
            return "QUIT"
        

    def show_team_info(self, team: object):
        """Shows team information for selected team
        returns: "BACK", "HOME", "QUIT" """

#=============== View team info menu interface ===============
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
#=============================================================

        choice = self.__prompt_options(["b", "h", "q"])

        if choice == "b":
            return "BACK"
        
        if choice == "h":
            return "HOME"
        
        return "QUIT"


    def show_tournament_info(self, tournament: object):
        """Shows tournament information for selected tournament
        returns: "VIEW SCHEDULE", "VIEW STANDINGS", "BACK", "HOME", "QUIT" """

#=============== View tournament info menu interface ===============
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
View {tournament.name} information

Name: {tournament.name}
Venue: {tournament.venue}
Start date: {tournament.startDate}
End date: {tournament.endDate}

Contact:
Email: {tournament.contactEmail}
Phone: {tournament.contactPhone}

1. View schedule
2. View results

b. Back
h. Home
q. Quit
""")
#===================================================================

        choice = self.__prompt_options(["1", "2", "b", "h", "q"])

        if choice == "1":
            return #TODO
        if choice == "2":
            return #TODO
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"


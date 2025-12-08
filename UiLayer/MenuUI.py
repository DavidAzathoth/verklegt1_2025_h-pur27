from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from LogicLayer.logicAPI import LogicAPI
from UiLayer.selectfrompage import SelectFromPage
from datetime import datetime, date
from Models.Team import Team
from Models.Player import Player

class MenuUI:
    def __init__(self, logic_api: LogicAPI):
        self.__logic_api = logic_api


#----------------------------------- Generic option prompts -----------------------------------------
    def __prompt_options(self, valid_options: list[str]):
        valid_lower = [i.lower() for i in valid_options]

        while True:
            choice = input("> ").strip().lower()

            if choice in valid_lower:
                return choice

            print(f"Invalid input. Valid options are: {'. '.join(valid_lower)}")


#----------------------------------- Set start and end date for tournament -----------------------------------------
    def set_start_end_date(self):
        while True:
            try:
                startdate = datetime.strptime(input("Tournament start date (YYYY-MM-DD): "), "%Y-%m-%d")
                
                enddate = datetime.strptime(input("Tournament end date (YYYY-MM-DD): "), "%Y-%m-%d")
                
            except ValueError:
                print("please enter valid numbers for year, month, day")
                continue

            if enddate < startdate:
                print("ERROR: End date must be after start date")
                continue

            print(f"Startdate: {startdate.date()} \nEnd date: {enddate.date()}")

            return startdate, enddate


#----------------------------------- Checks if player date of birth is valid -----------------------------------------
    def check_player_age(self):
        
        minimum_age = 18

        while True:
                try:
                    dob = datetime.strptime(input("Date of birth (YYYY-MM-DD): "), "%Y-%m-%d").date()
                except ValueError:
                    print("ERROR: Invalid input. Please enter a valid date")
                    continue
                
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

                if age < minimum_age:
                    print(f"ERROR: You must be at lease {minimum_age} years old. please enter a valid age")
                    continue

                break


#----------------------------------- MAIN MENU -----------------------------------------
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

            print("\n1. Continue\n2. Cancel\n")
            choice = self.__prompt_options(["1", "2"])

            while choice != "2":
                captain_handle: str = input("Handle: ")
                captain = self.__logic_api.getCaptain(captain_handle)

                if captain is False:
                    print("\nERROR: Captain is not registered into the system\n")
                    print("1. Continue\n2. Cancel")
                    choice = self.__prompt_options(["1", "2"])

                else:
                    if captain.get('hasTeam').strip() == 'True':
                        return ("CAPTAIN HAS TEAM", captain.get("captainHandle"))
                    else:
                        return ("CAPTAIN HAS NO TEAM", captain.get("captainHandle"))
                    
            return "BACK"
        return "QUIT"


#----------------------------------- TOURNAMENTS OPTIONS MENU (PUBLIC) -----------------------------------------       
    def show_tournaments_menu(self):
        """Prints tournaments options menu.
        returns: "PRINT LIST OF TOURNAMENTS", "SEARCH FOR A TOURNAMENT", "BACK", "QUIT" """
        
#========= TOURNAMENTS MENU INTERFACE ========
        print("""
---------------------------
 RU's e-sport Extravaganza 
---------------------------
Tournaments menu

1. Print list of tournaments
2. Search for tournament

b. Back
q. Quit
""")
#=======================================

        choice = self.__prompt_options(["1", "2", "b", "q"])

        if choice == "1":
            return "PRINT LIST OF TOURNAMENTS"
        if choice == "2":
            tournament_input = input("Please enter the tournament name: ")
            tournament = self.__logic_api.getTournamentbyName(tournament_input)
            while tournament == None:
                print("\nERROR: tournament name invalid.")
                print("\nContinue?")
                print("\ny. Yes (continue)")
                print("n. No (cancel)\n")

                choice = self.__prompt_options(["y", "n"])
                if choice == "y":
                    tournament_input = input("Please enter the tournament name: ")
                    tournament = self.__logic_api.getTournamentbyName(tournament_input)
                else: 
                    return "CANCEL"
                
            return ("GET TOURNAMENT", tournament)

        if choice == "b":
            return "BACK"
        
        return "QUIT"
    

#----------------------------------- TEAMS OPTIONS MENU (PUBLIC) -----------------------------------------
    def show_teams_menu(self):
        """Prints teams options menu
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
            team_input = input("Please enter the team name: ")
            team = self.__logic_api.searchforteam(team_input)
            while team == None:
                print("\nERROR: team name invalid.")
                print("\nContinue?")
                print("\ny. Yes (continue)")
                print("n. No (cancel)")

                choice = self.__prompt_options(["y", "n"])
                if choice == "y":
                    team_input = input("Please enter the team name: ")
                    team = self.__logic_api.searchforteam(team_input)
                else: 
                    return "CANCEL"
                
            return ("GET TEAM", team)

        if choice == "b":
            return "BACK"
        
        return "QUIT"


#----------------------------------- ORGANIZER MENU -----------------------------------------
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
5. Register a new team captain

b. Back
q. Quit""")
#=========================================
        
        choice = self.__prompt_options(["1", "2", "3", "4", "5", "b", "q"])

        if choice == "1":
            return "CREATE TOURNAMENT"
        if choice == "2":
            return "ADD TEAMS TO TOURNAMENT"
        if choice == "3":
            return "GENERATE SCHEDULE"
        if choice == "4":
            return "UPDATE RESULTS"
        if choice == "5":
            while True:
                captain_handle = input("Please enter captain handle here: ").strip()
                
                #Ef team captain er núþegar til þá ERROR
                if self.__logic_api.getCaptain(captain_handle):
                    print("ERROR: Team captain already exists, please try again.")
                    continue
                #Annars býr til team captain

                else:
                    print()
                    print("-" * 50)
                    print(f"Team captain {captain_handle} can be registered.")
                    print("\nconfirm?\n")
                    print("y. Yes, confirm")
                    print("n. No, cancel")

                    choice = self.__prompt_options(["y", "n"])
                    if choice == "y":
                        self.__logic_api.registerCaptain(captain_handle)
                        print(f"\nTeam captain: {captain_handle} has been registered")
                        print("\nPress ENTER to Go back\n")
                        choice = self.__prompt_options([""])
                    return"CANCEL"
                
        if choice == "b":
            return "BACK"
        return "QUIT"

   
#----------------------------------- CAPTAIN MENU (NO TEAM) -----------------------------------------
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


#----------------------------------- CAPTAIN MENU (HAS TEAM) -----------------------------------------
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
    

#----------------------------------- TOURNAMENT CREATION MENU (ORGANIZER) -----------------------------------------
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
        print(("ContactEmail: "), contactemail)
        contactphone = int(input("ContactPhone: ").strip())

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
    

#----------------------------------- TEAM CREATION MENU (CAPTAIN) -----------------------------------------
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

        team_name = input("Team name: ").strip()
#=======================================================

        #Use search for team to check duplicates
        check_team_duplicate = self.__logic_api.searchforteam((team_name))

        #repeats until team name is unique and nonempty
        while check_team_duplicate != None or team_name == "":

            if team_name == "":
                print("\nPlease enter a valid name")
                team_name = input("Team name: ").strip()
                check_team_duplicate = self.__logic_api.searchforteam((team_name))

            else:
                print("\nERROR: Team name already exists, please try another name")
                team_name = input("Team name: ").strip()
                check_team_duplicate = self.__logic_api.searchforteam((team_name))

        teamID = len(self.__logic_api.getTeams()) + 1
        newteam = self.__logic_api.createteam([teamID, team_name])
        print("""
1. Add players to team
2. Cancel
""")
        choice = self.__prompt_options(["1", "2"])
        if choice == "1":
            return ("PLAYER CREATION", newteam, captain_handle)
        return "CANCEL"


#----------------------------------- PLAYER CREATION MENU (CAPTAIN) -----------------------------------------
    def show_player_creation_menu(self, team: Team, captain_handle: str):
        """Displays the player creation menu interface"""
        
        #stores players before creating
        player_list: list[Player] = []
        player_count = 1
        while player_count != 5:

#============ PLAYER CREATION MENU INTERFACE =============
            print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Player creation menu
                  
Add player {player_count}
""")
#=========================================================
            
            #Fill in list for player, first player is team captain
            if player_count == 1:
                handle = captain_handle
                print(f"player handle: {handle}")
            else:
                handle = input("Player handle: ").strip()
            name = input("Player name: ").strip()
            dob = self.check_player_age()
            address = input("Player address: ")
            phone_num = int(input("Player phone number: ").strip())
            teamID = len(self.__logic_api.getTeams()) + 1
            
            check_player_email: tuple = self.__logic_api.emailVerification(input("Player Email: "))
            while check_player_email[1] == False:
                print(check_player_email[0])
                check_player_email: tuple = self.__logic_api.emailVerification(input("Player Email: "))
            playeremail = check_player_email[0]
            print(("Player Email: "), playeremail)

            link = input("Player link: ").strip()

            #confirm player creation
            print(f"""
Create player {handle}?

1. Yes
2. Cancel                  
""")
            choice = self.__prompt_options(["1", "2"])
            if choice == "1":
                player = self.__logic_api.createPlayer([teamID, handle, name, phone_num, playeremail, address, link, dob])
                player_list.append(player)
                player_count += 1
            else:
                return "CANCEL"
            
            if player_count < 3:
                continue
                
            else: 
                print("""
1. Add another player?
2. Confirm creation
3. Cancel
""")
                choice = self.__prompt_options(["1", "2", "3"])
                if choice == "1":
                    continue
                if choice == "2":
                    for player in player_list:
                        self.__logic_api.savePlayer(player)
                        self.__logic_api.addplayer(player, team)
                return "CANCEL"
        
        print("""
1. Confirm creation
2. Cancel              
""")
        choice = self.__prompt_options(["1", "2"]) 
        if choice == "1":
            return #TODO save information
        return "CANCEL"
            
                

            


        totalTeams = self.__logic_api.getTeams()
        newTeam = self.__logic_api.createteam([])
        newPlayer = self.__logic_api.createPlayer([])
        self.__logic_api.savePlayer(newPlayer)
        # TODO CREATE TEAM AND PLAYER MENU


#----------------------------------- VIEW ALL TEAMS MENU (PUBLIC) -----------------------------------------
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


#----------------------------------- VIEW ALL TOURNAMENTS MENU (PUBLIC) -----------------------------------------    
    def show_view_tournaments_menu(self):
        """Prints list of tournaments
        returns: ("TOURNAMENT INFO",  tournament: object), "BACK", "QUIT"  """
        
        tournaments = self.__logic_api.gettournaments()

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
        

#----------------------------------- TEAM INFO MENU (PUBLIC) -----------------------------------------
    def show_team_info(self, team: Team):
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


#----------------------------------- TOURNAMENT INFO MENU (PUBLIC) -----------------------------------------
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
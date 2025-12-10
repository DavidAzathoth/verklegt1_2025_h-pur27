from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from LogicLayer.logicAPI import LogicAPI
from UiLayer.selectfrompage import SelectFromPage
from datetime import datetime, date
from Models.Team import Team
from Models.Player import Player
from Models.Tournament import Tournament
from Models.Bracket import Bracket
import time
import sys

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
                    print(f"ERROR: You must be at least {minimum_age} years old. please enter a valid age")
                    continue

                break
        return dob


#----------------------------------- Saves team, player and captain info --------------------------------------------
    def save_player_and_team(self, player_list: list[Player], team: Team, captain_handle: str):
        for player in player_list:
            self.__logic_api.savePlayer(player)

        self.__logic_api.saveTeam(team)

        self.__logic_api.addplayers(player_list, team)

        self.__logic_api.updatecaptain(captain_handle)

        print()
        print("-" * 30)
        print("Team has successfully been created!\n")
        print("Going back to captain menu...\n")
        print("Press ENTER to continue")


#----------------------------------- Slow print --------------------------------------------
    def slow_print(self, text, delay = 0.05):
        """Prints a string slowly instead of instantly"""

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()



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

            while True:
                captain_handle_input: str = input("Handle: ")
                captain_dict = self.__logic_api.getCaptain(captain_handle_input)

                if captain_dict is False:
                    print()
                    print("-" * 50)
                    print("ERROR: Captain is not registered into the system")
                    print("\nTry again?\n")
                    print("ENTER. Try again\nc. Cancel")
                    
                    choice = self.__prompt_options(["", "c"])
                    if choice == "":
                        continue
                    return "BACK"

                else:
                    if captain_dict.get('hasTeam').strip() == 'True':
                        captain_handle = captain_dict.get("captainHandle")
                        team = self.__logic_api.get_team_by_captain(captain_handle)
                        return ("CAPTAIN HAS TEAM", captain_handle, team)
                    else:
                        return ("CAPTAIN HAS NO TEAM", captain_handle)
                    
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
            tournament = self.__logic_api.gettournamentbyname(tournament_input)
            while tournament == None:
                print("-" * 33)
                print("\nERROR: tournament name invalid.")
                print("\nTry again?")
                print("\nENTER. Try again")
                print("c. Cancel\n")

                choice = self.__prompt_options(["", "c"])
                if choice == "":
                    tournament_input = input("Please enter the tournament name: ")
                    tournament = self.__logic_api.gettournamentbyname(tournament_input)
                else: 
                    return "CANCEL"
                
            return ("GET TOURNAMENT", tournament)

        if choice == "b":
            return "BACK"
        
        return "QUIT"
    

#----------------------------------- TEAMS OPTIONS MENU (PUBLIC) -----------------------------------------
    def show_teams_menu(self):
        """Prints teams options menu.
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
                    print("\nERROR: Team captain already exists, please try again.\n")
                    print("1. Try again\n2. Cancel\n")
                    choice = self.__prompt_options(["1", "2"])
                    if choice == "1":
                        continue
                    return "CANCEL"


                #Annars býr til team captain
                else:
                    print()
                    print("-" * 60)
                    print(f"Team captain {captain_handle} can be registered.")
                    print("\nconfirm?\n")
                    print("1. Yes, confirm")
                    print("2. No, cancel")

                    choice = self.__prompt_options(["1", "2"])
                    if choice == "1":
                        self.__logic_api.registerCaptain(captain_handle)
                        print("-" * 60)
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
{captain_handle}'s Menu

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
    def show_captain_has_team_menu(self, captain_handle: str, team: Team):
        """Prints out captain menu if has team"""

#========= CAPTAIN HAS TEAM MENU INTERFACE =========
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{captain_handle}'s Menu

1. View my team/players
2. Edit team information

b. Back
q. Quit
""")
#===================================================
        
        choice = self.__prompt_options(["1", "2", "b", "q"])
        if choice == "1":
            return ("VIEW MY TEAM/PLAYERS", team)
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

        #Input repeats until team name is unique and nonempty
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
        newteam.captainHandle = captain_handle

        print("""
1. Add players to team
2. Cancel
""")
        choice = self.__prompt_options(["1", "2"])
        if choice == "1":
            return ("PLAYER CREATION", newteam, newteam.captainHandle)
        return "CANCEL"


#----------------------------------- PLAYER CREATION MENU (CAPTAIN) -----------------------------------------
    def show_player_creation_menu(self, team: Team, captain_handle: str):
        """Displays the player creation menu interface"""
        
        #stores players before saving to file
        player_list: list[Player] = []
        player_count = 0

        #Loops until player count == 5
        while player_count != 5:

#==PLAYER CREATION MENU INTERFACE ====
            print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Player creation menu
                  
Add player {player_count + 1}:
""")
#=================================
            
            #Fill in list for player. The first player is always team captain
            if player_count == 0:
                handle = captain_handle
                print(f"player handle (captain): {handle}")
            else:
                #Checks if handle is already used
                while True:
                    handle = input("Player handle: ").strip()
                    team_handles = [p.playerGamertag.lower() for p in player_list]
                    handle_check = self.__logic_api.getPlayer_by_gamertag(handle)
                    
                    if handle_check is not None or handle.lower() in team_handles:
                        print("\nERROR: player handle already exists. Please enter a new one\n")
                        continue
                
                    break

            #Real name
            name = input("Player name: ").strip()
            #Date of birth
            dob = self.check_player_age()
            #Home address
            address = input("Player address: ").strip()

            #Phone number loop
            while True:
                try:
                    phone_num = int(input("Player phone number: ").strip())
                    break
                except ValueError:
                    print("\nERROR: Please enter a valid phone number\n")

            #TeamID        
            teamID = team.teamID
            
            #Confirm player email
            check_player_email: tuple = self.__logic_api.emailVerification(input("Player Email: "))
            while check_player_email[1] == False:
                print(check_player_email[0])
                check_player_email: tuple = self.__logic_api.emailVerification(input("Player Email: "))
            playeremail = check_player_email[0]
            print(("-Confirmed player email:"), playeremail)

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
                print(f"Player {handle} has been created!")
                print("-" * 45)
            else:
                return "CANCEL"
            
            if player_count < 3:
                print("\nPress ENTER to go to next player (MIN = 3)")
                choice = self.__prompt_options([""])
                continue
                
            elif player_count != 5: 
                print("""
1. Add another player?
2. Confirm creation
3. Cancel
""")
                choice = self.__prompt_options(["1", "2", "3"])
                if choice == "1":
                    continue

                if choice == "2":

                    self.save_player_and_team(player_list, team, captain_handle)
                    
                    self.__prompt_options([""])
                    return  "CONTINUE"
                
                return "CANCEL"
        
        print("""
1. Confirm creation
2. Cancel              
""")
        choice = self.__prompt_options(["1", "2"]) 
        if choice == "1":
            
            self.save_player_and_team(player_list, team, captain_handle)

            self.__prompt_options([""])
            return "CONTINUE"
        
        return "CANCEL"


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
                team = self.__logic_api.searchforteam(team_name)
                
                return ("TEAM INFO", team)
                
            
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

#======LIST OF TOURNAMENTS INTERFACE======
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
#=========================================
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
        

#----------------------------------- TEAM INFO MENU (PUBLIC/CAPTAIN) -----------------------------------------
    def show_team_info(self, team: Team, mode: str):
        """Shows team information for selected team.\n
        Returns: "BACK", "HOME", "QUIT"\n
        Modes: "SEARCH TEAM", "VIEW TEAMS", "CAPTAIN" """
        
        ##If viewing from public
        if mode in ("SEARCH TEAM", "VIEW TEAMS"):

#=============== View team info menu interface (public) ===============
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

        ##If viewing from captain menu
        elif mode == "CAPTAIN":
            viewer = SelectFromPage(team.roster)
            while True:
#========== View team info menu interface (Captain) ==========
                print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{team.captainHandle}'s team information

Name: {team.teamName}
Captain: {team.captainHandle}

Player handles:
{viewer.currentPage()}            
        
Wins: {team.wins}
Losses: {team.losses}

1-5. View player
b. Back
q. Quit
""")
#=============================================================
                choice = self.__prompt_options(["1", "2", "3", "4", "5", "b", "q"])

                if choice.isdigit():
                    num = int(choice)

                    player_name = viewer.select_item_by_number(num)

                    try:
                        player = self.__logic_api.getPlayer_by_gamertag(player_name)
                    except:
                        continue

                    return("PLAYER INFO", player)
                
                elif choice == "b":
                    return "BACK"
                return "QUIT"


#----------------------------------- TOURNAMENT INFO MENU (PUBLIC) -----------------------------------------
    def show_tournament_info(self, tournament: Tournament):
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
            return "VIEW SCHEDULE"
        if choice == "2":
            return "VIEW RESULTS"
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"
    

#----------------------------------- ADD TEAMS TO TOURNAMENT MENU (ORGANIZER)) -----------------------------------------
    def show_add_teams_to_tournament_menu(self, tournament: Tournament):
        """displays menu to add teams into specified tournament"""

        self.__logic_api.populateTournament(tournament)


        #print 5 items per page loop
        while True:

            print(f"""
----------------------------------------
 RU's e-Sport Extravaganza
----------------------------------------
Add teams to tournament: {tournament.name}

Teams currently registered:
""")
            
            registered_teams: list[Team] = tournament.teams
            try:
                for team in registered_teams:
                    print("-", team.teamName)
            except:
                print("- No teams have been registered")

            available_teams: list[Team] = self.__logic_api.availableteams(tournament)

            team_names = [t.teamName.strip() for t in available_teams]

            viewer = SelectFromPage(team_names)

            print(f"""
Available teams:
                  
{viewer.currentPage()}

ENTER. Next page
1-5. Add team
b. Back
h. Home (Organizer)
q. Quit 
""")

            choice = self.__prompt_options(["1", "2", "3", "4", "5", "", "h", "b", "q"])

            #select team by number
            if choice.isdigit():
                num = int(choice)
                team_name = viewer.select_item_by_number(num)

                # find team object
                for t in available_teams:
                    if t.teamName == team_name:
                        self.__logic_api.addTeamtoTournament(t, tournament)
                continue

            if choice ==  "":
                viewer.next_page()
                continue

            if choice == "b":
                return "BACK"
            
            if choice == "h":
                answer = "HOME"
                break
            
            return "QUIT"
        return answer


#----------------------------------- SCHEDULE GENERATION MENU (ORGANIZER)) -----------------------------------------
    def show_generate_schedule_menu(self, tournament: Tournament):
        """Displays the menu where the schedule is generated"""
        
        self.__logic_api.populateTournament(tournament)
        current_teams = len(tournament.teams)
        minimum_teams = 16

        #Checking if enough teams
        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------""")    
        self.slow_print("Checking team count...\n", 0.1)          
        
        self.slow_print(f"Current number of teams: {current_teams}\n")
        
        self.slow_print(f"Minimum teams required: {minimum_teams}\n")
        
        self.slow_print(f".....\n", 0.3)
        
        if current_teams < minimum_teams:
            #Error path: not enough teams
            print("""
ERROR: Not enough teams to generate bracket
                  
Please add more teams to this tournament

1. Go to "Add teams to tournament" menu
2. Back to Organizer menu                  
                  """)
            
            choice = self.__prompt_options(["1", "2"])
            if choice == "1":
                return ("GO TO ADD TEAMS TO TOURNAMENT", tournament)
            return "CANCEL"
        
        else:
            #number of teams is enough
            print("""
This tournament has sufficient teams!                  

1. Generate schedule
2. Cancel
""")
            choice = self.__prompt_options(["1", "2"])

            if choice == "1":
                print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------""")    
                
                generate = (f"Generating schedule...\n", f"\nSchedule has been generated!\n", f"\nThis is the schedule for: {tournament.name}\n")
                for s in generate:
                    self.slow_print(s)
                
                self.__logic_api.generatebracket(tournament)
                
                self.__logic_api.saveBracket(tournament.bracket)

                bracket: Bracket = tournament.bracket

                self.__logic_api.populateBracket(bracket)

                for i, round in bracket.rounds.items():
                    print(f"Round {i}:")
                    print("-" * 70)
                    print()
                    for match in round:
                        print(match)
                    print()
                    print("-" * 70)
                    
                
                
                return "QUIT"



            return "CANCEL"
        

#----------------------------------- PLAYER INFO MENU (CAPTAIN)) -----------------------------------------
    def show_player_info_menu(self, player: Player):
        """Displays options to edit specific player information.\n
        Returns: "BACK", "CAPTAIN MENU", "QUIT" """
        
        while True:
            print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
                  
{player.playerGamertag}'s personal information
-----------------------------------------------

Handle:        {player.playerGamertag}
Name:          {player.fullname}
Date of Birth: {player.dateOfBirth}
Address:       {player.address}
Phone number:  {player.phoneNumber}
Email:         {player.emailAddress}
Link:          {player.link}

------------------------------------------------

1. Edit player info

b. Back
h. Captain menu
q. Quit

""")
            choice = self.__prompt_options(["1", "b", "h", "q"])

            if choice == "1":
                attributes = [["address", "phoneNumber", "emailAddress", "link"]]
                viewer = SelectFromPage(attributes)

                #Edit options for player
                print(f"""
------------------------------------------------
Edit player information: {player.playerGamertag}
------------------------------------------------
1. Edit Address
2. Edit Phone
3. Edit Email
4. Edit Link

c. Cancel
""")
                
                edit_choice = self.__prompt_options(["1", "2", "3", "4", "c"])

                if edit_choice.isdigit():

                    num = int(edit_choice)
                    attribute = viewer.select_item_by_number(num)
                    new_value = input("""Please enter new value or press "c" (Cancel): """.strip())
                    if new_value.lower() == "c":
                        continue
                    while True:
                        try:
                            self.__logic_api.editplayer(player.playerGamertag, attribute, new_value)
                            break
                        except ValueError or TypeError:
                            print(f"\nERROR: Please enter correct value for player {attribute}.\n")
                    
                    print(f"\n{attribute} has been updated!\n")
                    print("Returning to player info menu\n")
                    self.slow_print("....", 0.3)
                    continue

                #Cancel
                continue

            if choice == "b":
                return "BACK"
                
            
            if choice == "h":
                return "CAPTAIN MENU"
            
            return "QUIT"


#----------------------------------- TOURNAMENT SCHEDULE MENU (PUBLIC) -----------------------------------------
    def show_tournament_schedule(self, tournament: Tournament):
        """Displays the tournament schedule menu for public  view\n
        Returns: "BACK", "HOME", "QUIT" """

        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------

Tournament schedule for: {tournament.name}
{print("-" * 70)}
""")
        
        self.__logic_api.populateTournament(tournament)
        
        bracket: Bracket = tournament.bracket

        for i, round in bracket.rounds.items():
                    print(f"Round {i}:")
                    print("-" * 70)
                    print()
                    for match in round:
                        print(match)
                    print()
                    print("-" * 70)

        choice = self.__prompt_options(["b", "h", "q"])
        
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"
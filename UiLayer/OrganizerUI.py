from Models.Team import Team
from LogicLayer.logicAPI import LogicAPI
from UiLayer.selectfrompage import SelectFromPage
from UiLayer.PrintMatches import PrintMatches
from UiLayer.BaseUI import BaseUI
from Models.Tournament import Tournament
from Models.Bracket import Bracket
from Models.Match import Match
from LogicLayer.menuLogic import InvalidEmailError
import time

class OrganizerUI:
    def __init__(self, logic_api: LogicAPI, base_ui: BaseUI):
        self.__logic_api = logic_api
        self.baseUI = base_ui



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
        
        choice = self.baseUI.prompt_options(["1", "2", "3", "4", "5", "b", "q"])
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
                    choice = self.baseUI.prompt_options(["1", "2"])
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

                    choice = self.baseUI.prompt_options(["1", "2"])
                    if choice == "1":
                        self.__logic_api.registerCaptain(captain_handle)
                        print("-" * 60)
                        print(f"\nTeam captain: {captain_handle} has been registered")
                        print("\nPress ENTER to Go back\n")
                        choice = self.baseUI.prompt_options([""])
                    return"CANCEL"
                
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
        existing_tournament = self.__logic_api.getTournamentbyName(name)
        
        #Loops and prompts new name if name exists already
        while isinstance(existing_tournament, Tournament):
            print()
            print("-" * 50)
            print("ERROR: A tournament already exists with this name\n")
            name: str = input("Name: ").strip()
            existing_tournament = self.__logic_api.getTournamentbyName(name)            

        
        #start, enddate for tournament
        while True:
            startdate_input = input("Tournament start date (YYYY-MM-DD): ")
            enddate_input = enddate = input("Tournament end date (YYYY-MM-DD): ")
            try:
                result = self.__logic_api.set_start_end_date(startdate_input, enddate_input)
                
                if result is None:
                    print("\nERROR: End date must be after start date\n")
                    continue

                startdate, enddate = result
                break
            
            except ValueError:
                print("\nERROR: please enter valid numbers for year-month-day\n")
        
        #ContactEmail
        while True:
            try:
                contactemail, valid = self.__logic_api.emailVerification(input("ContactEmail: "))
                if valid is InvalidEmailError:
                    raise InvalidEmailError(contactemail)
                print(("-Confirmed ContactEmail: "), contactemail)
                break
            
            except InvalidEmailError as contactemail:
                print()
                print("-" * 60)
                print(contactemail)
                        
        
        #Contactphone
        while True:
            try:
                contactphone = int(input("ContactPhone: ").strip())
                break
            except ValueError:
                print()
                print("-" * 40)
                print("ERROR: Please enter a valid phone number\n")

#===========================================================

        # Asks to input informattion to create tournament
        tournament: Tournament = self.__logic_api.createtournament([venue, name, startdate.date(), enddate.date(), contactemail, contactphone])

        #self.__logic_api.saveTournament(tournament) <--- saves tournament
        print("""

1. Confirm creation
c. Cancel
""")
        choice = self.baseUI.prompt_options(["1", "c"])
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
        
        choice = self.baseUI.prompt_options(["b", "h", "q"])
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"


    def show_add_teams_to_tournament_menu(self, tournament: Tournament):
        """displays menu to add teams into specified tournament"""

        if self.__logic_api.validateTournamentBracket(tournament) == True:
            print('You can not add teams to an already active tournament!')
            return "BACK"
        
        #print 5 items per page loop
        while True:
            registered_teams: list[Team] = tournament.teams

            print(f"""
----------------------------------------
 RU's e-Sport Extravaganza
----------------------------------------
Add teams to tournament: {tournament.name}

Teams currently registered: {len(registered_teams)}
""")
            
            try:
                for team in registered_teams:
                    print("-", team.teamName)
            except:
                print("- No teams have been registered")

            available_teams: list[Team] = self.__logic_api.availableteams(tournament)

            team_names = [t.teamName.strip() for t in available_teams]
            try:
                viewer.items = team_names
            except:
                viewer = SelectFromPage(team_names)

            print(f"""
Available teams:
                  
{viewer.currentPage()}

ENTER. Next page
1-5. Add team
b. Back
h. Organizer menu
q. Quit 
""")

            choice = self.baseUI.prompt_options(["1", "2", "3", "4", "5", "", "h", "b", "q"])

            #select team by number
            if choice.isdigit():
                num = int(choice)
                team_name = viewer.select_item_by_number(num)

                # find team object
                for t in available_teams:
                    if t.teamName == team_name:
                        if self.__logic_api.addTeamtoTournament(t, tournament):
                            pass
                        else:
                            print("""
                                  
#######################################################################
ERROR: Tournament has a generated bracket, adding teams is not possible
#######################################################################""")

                            return "BACK"
                            
                continue

            if choice ==  "":
                viewer.next_page()
                continue

            if choice == "b":
                return "BACK"
            
            if choice == "h":
                return "ORGANIZER"
            
            return "QUIT"


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
        self.baseUI.slow_print("Checking team count\n")      

        self.baseUI.slow_print("....", 0.3)    
        
        self.baseUI.slow_print(f"\nCurrent number of teams: {current_teams}\n")
        
        self.baseUI.slow_print(f"Minimum teams required: {minimum_teams}\n")
        
        self.baseUI.slow_print(f"....\n", 0.3)
        
        if current_teams < minimum_teams:
            #Error path: not enough teams
            print("""
ERROR: Not enough teams to generate bracket
                  
Please add more teams to this tournament

1. Go to "Add teams to tournament" menu
2. Back to Organizer menu                  
                  """)
            
            choice = self.baseUI.prompt_options(["1", "2"])
            if choice == "1":
                return "ADD TEAMS TO TOURNAMENT"
            return "ORGANIZER"
        
        else:
            #number of teams is enough
            print("""
This tournament has sufficient teams!                  

1. Generate schedule
2. Cancel
""")
            choice = self.baseUI.prompt_options(["1", "2"])

            if choice == "1":
                print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------""")    
                server = 1
                while True:
                    try:
                        generate_bracket = self.__logic_api.generatebracket(tournament, server)
                        break
                    except IndexError:
                    #Adds another server if tournament is too short
                        server+=1

                if generate_bracket == False:
                    
                    self.baseUI.slow_print("\nERROR: Bracket has already been generated for this tournament\n")
                    self.baseUI.slow_print("Going back to List of tournaments\n")
                    time.sleep(1)
                    return "BACK"
                
                
                generate = (f"Generating schedule...\n", f"\nSchedule has been generated!\n", f"\nThis is the schedule for: {tournament.name}\n")
                for s in generate:
                    self.baseUI.slow_print(s)
                
                self.__logic_api.saveBracket(tournament.bracket)

                bracket: Bracket = tournament.bracket
                
                self.__logic_api.populateBracket(bracket)

                printer = PrintMatches(tournament) 
                printer.print_schedule_table()
                    
                self.__logic_api.updateTournament(tournament)

                
                print("""
b. Back
h. ORGANIZER
q. Quit
""")
                choice = self.baseUI.prompt_options(["b", "h", "q"])
                
                if choice == "b":
                    return "BACK"
                if choice == "h":
                    return "ORGANIZER"
                return "QUIT"



            return "BACK"


    def show_update_results_menu(self, tournament: Tournament):
        """Shows menu to update tournament information for organizer"""

        if self.__logic_api.validateTournamentBracket(tournament) == False:
            print('Tournament has no bracket!')
            return "BACK"
        
        while True:
            
            updatable_matches: list[Match] = self.__logic_api.geteligibleMatches(tournament)
            
            # Gets updated list of matches if viewer was initialized
            try:
                viewer.items = updatable_matches
            except:
                viewer = SelectFromPage(updatable_matches)

            print(f"""
----------------------------------------------------
 RU's e-Sport Extravaganza
----------------------------------------------------
Select a match to update results for {tournament.name}

Unfinished matches:
-----------------------------------------
{viewer.currentPage()}
-----------------------------------------

ENTER. Next page
1-5. Select match
b. Back
h. Organizer menu
q. Quit 
""")    
            choice = self.baseUI.prompt_options(["1", "2", "3", "4", "5", "", "b", "h", "q"])
            if choice == "":
                viewer.next_page()
                continue
            if choice == "b":
                return "BACK"
            if choice == "h":
                return "HOME"
            if choice == "q":
                return "QUIT"
            if choice.isdigit():
                num = int(choice)

                #returns the selected match
                match: Match | None = viewer.select_item_by_number(num)
                
                #if can't find match
                if match is None:
                    continue

                print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------                      
Update results for match: {match.matchID}

Teams: {match.team_A} vs {match.team_B}
Date: {match.matchDate}, {match.matchTime}

Scores:""")
                print("-" * 40)

            # Validate team score inputs
                while True:
                    try:
                        team_A_score = int(input(f"Enter score for {match.team_A}: ").strip())
                        team_B_score = int(input(f"Enter score for {match.team_B}: ").strip())
                        
                        winner = self.__logic_api.returnMatchWinner(match, team_A_score, team_B_score)
                        
                        if not winner:
                            print('\nERROR: Match cannot be a tie\n')
                            continue
                        break   
                    except ValueError:
                        print()
                        print("-" * 35)
                        print("ERROR: Please enter a valid integer\n")

                print(f"""
-------------------------------------------
Confirm update for match {match.matchID}?

Winner: {winner}


1. Confirm
c. Cancel

h. Organizer menu
q. Quit
""")
                choice = self.baseUI.prompt_options(["1", "c", "h", "q"])
                if choice == "1":
                    score = [team_A_score, team_B_score]
                    self.__logic_api.confirmMatchWinner(tournament, match, score)
                    tournament = self.__logic_api.reloadTournament(tournament)
                elif choice == "c":
                    continue
                elif choice == "h":
                    return "HOME"
                elif choice == "q":
                    return "QUIT"
            continue

from Models.Team import Team
from LogicLayer.logicAPI import LogicAPI
from UiLayer.selectfrompage import SelectFromPage
from UiLayer.PrintMatches import PrintMatches
from UiLayer.BaseUI import BaseUI
from Models.Tournament import Tournament


class PublicUI:
    def __init__(self, logic_api: LogicAPI, base_ui: BaseUI):
        self.__logic_api = logic_api
        self.baseUI = base_ui


    def show_tournaments_menu(self):
        """Prints view tournaments options menu.\n
        Returns: "PRINT LIST OF TOURNAMENTS", ("GET TOURNAMENT", Tournament), "CANCEL", "BACK", "QUIT" """

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

        choice = self.baseUI.prompt_options(["1", "2", "b", "q"])

        if choice == "1":
            return "PRINT LIST OF TOURNAMENTS"
        if choice == "2":
            tournament_input = input("Please enter the tournament name: ")
            tournament = self.__logic_api.getTournamentbyName(tournament_input)
            while tournament == None:
                print("-" * 33)
                print("\nERROR: tournament name invalid.")
                print("\nTry again?")
                print("\nENTER. Try again")
                print("c. Cancel\n")

                choice = self.baseUI.prompt_options(["", "c"])
                if choice == "":
                    tournament_input = input("Please enter the tournament name: ")
                    tournament = self.__logic_api.getTournamentbyName(tournament_input)
                else: 
                    return "CANCEL"
                
            return ("GET TOURNAMENT", tournament)

        if choice == "b":
            return "BACK"
        
        return "QUIT"


    def show_teams_menu(self):
        """Prints view teams options menu.\n
        returns: "PRINT LIST OF TEAMS", ("GET TEAM", Team), "CANCEL", "BACK", "QUIT" """

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
 
        choice = self.baseUI.prompt_options(["1", "2", "b", "q"])

        if choice == "1":
            return "PRINT LIST OF TEAMS"
        if choice == "2":
            team_input = input("Please enter the team name: ")
            team = self.__logic_api.searchforteam(team_input)
            while team == None:
                print()
                print("-" * 28)
                print("ERROR: team name invalid.")
                print("\nTry again?")
                print("\nENTER. Try again")
                print("c. Cancel")

                choice = self.baseUI.prompt_options(["", "c"])
                if choice == "":
                    team_input = input("Please enter the team name: ")
                    team = self.__logic_api.searchforteam(team_input)
                else: 
                    return "CANCEL"
                
            return ("GET TEAM", team)

        if choice == "b":
            return "BACK"
        
        return "QUIT"


    def show_view_teams_menu(self):
        """Shows list of 5 teams at a time. allows to view team info.\n
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

            choice = self.baseUI.prompt_options(["1", "2", "3", "4", "5", "", "b", "q"])

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


    def show_view_tournaments_menu(self, mode):
        """Prints list of tournaments.\n
        modes: "VIEW TOURNAMENTS"(public), "ADD TEAMS"(organizer), "GENERATE"(organizer), "UPDATE"(organizer)\n
        returns: ("TOURNAMENT",  tournament: object), "BACK", "QUIT"  """
        
        # view what kind of mode the menu is in (public/organizer)
        if mode == "VIEW TOURNAMENTS":
            view_mode = "PUBLIC"
        else:
            view_mode = mode

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
                  
View mode: {view_mode.title()}
              
{viewer.currentPage()}
              
ENTER. Next page
1-5. Select tournament
b. Back
q. Quit              
""") 
#=========================================
            choice = self.baseUI.prompt_options(["1", "2", "3", "4", "5", "", "b", "q"])

            #select tournament by number
            if choice.isdigit():
                num = int(choice)
                tournament_name = viewer.select_item_by_number(num)
                
                # find tournament object
                for t in tournaments:
                    if t.name == tournament_name:
                        return ("TOURNAMENT", t)
                continue
            
            #press ENTER to go to next page
            if choice ==  "":
                viewer.next_page()
                continue

            if choice == "b":
                return "BACK"
            
            return "QUIT"


    def show_team_info(self, team: Team, mode: str):
        """Shows team information for selected team.\n
        modes: "SEARCH TEAM"(public), "VIEW TEAMS"(public), "CAPTAIN"\n 
        returns: "BACK", "HOME", "QUIT", ("PLAYER INFO", player) """
        
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

            choice = self.baseUI.prompt_options(["b", "h", "q"])

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
                choice = self.baseUI.prompt_options(["1", "2", "3", "4", "5", "b", "q"])

                if choice.isdigit():
                    num = int(choice)

                    player_name = viewer.select_item_by_number(num)

                    try:
                        player = self.__logic_api.getPlayer_by_gamertag(player_name)
                    except:
                        continue

                    return("PLAYER INFO", player)
                
                if choice == "b":
                    return "BACK"
                return "QUIT"


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

        choice = self.baseUI.prompt_options(["1", "2", "b", "h", "q"])

        if choice == "1":
            return "VIEW SCHEDULE"
        if choice == "2":
            return "VIEW RESULTS"
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"


    def show_tournament_schedule(self, tournament: Tournament):
        """Displays the tournament schedule menu for public  view\n
        Returns: "BACK", "HOME", "QUIT" """
        if self.__logic_api.validateTournamentBracket(tournament) == False:
            print('Tournament has no bracket!')
            return "BACK"
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------

Tournament schedule for: {tournament.name}
""")
        
        printer = PrintMatches(tournament)
        printer.print_schedule_table()

        print("""
b. Back
h. Home
q. Quit
""")
        choice = self.baseUI.prompt_options(["b", "h", "q"])
        
        if choice == "b":
            return "BACK"
        if choice == "h":
            return "HOME"
        return "QUIT"


    def show_view_tournament_results_menu(self,tournament: Tournament):
        """Displays the tournament standings for selected tournament"""
        if self.__logic_api.validateTournamentBracket(tournament) == False:
            print('Tournament has no bracket!')
            return "BACK"
        
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Full standings - {tournament.name}
""")
        printer = PrintMatches(tournament)
        printer.print_results_table()

        print("""
b. Back
h. Home
q. Quit
""")    
        choice = self.baseUI.prompt_options(["b", "h", "q"])
        if choice == "b":
            return "BACK"
        
        if choice == "h":
            return "HOME"
        
        return "QUIT"


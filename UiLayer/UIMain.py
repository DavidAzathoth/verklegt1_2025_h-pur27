from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI

class UIMain:
    def __init__(self) -> None:
        logic_api = LogicAPI()
        self.__menu_ui =  MenuUI(logic_api)
        self.current_screen = "MAIN MENU"
        self.selection_mode = None

    def mainloop(self) -> None:
        """Main loop of the menus"""
        while True:

#============================= MAIN MENU LOOP =======================
            if self.current_screen == "MAIN MENU":
                options: str = self.__menu_ui.show_main_menu()
                if options == "TOURNAMENTS":
                    self.current_screen = "TOURNAMENTS MENU"

                elif options == "TEAMS":
                    self.current_screen = "TEAMS MENU"

                elif options == "ORGANIZER":
                    self.current_screen = "ORGANIZER MENU"

                elif isinstance(options, tuple) and options[0] == "CAPTAIN HAS NO TEAM":
                    captain_handle = options[1]
                    self.captain_handle = captain_handle
                    self.current_screen = "CAPTAIN HAS NO TEAM MENU"

                elif isinstance(options, tuple) and options[0] == "CAPTAIN HAS TEAM":
                    captain_handle = options[1]
                    self.captain_handle = captain_handle
                    self.current_screen = "CAPTAIN HAS TEAM MENU"

                elif options == "BACK":
                    self.current_screen = "MAIN MENU"

                elif options == "QUIT":
                    break

#============================= TOURNAMENTS MENU LOOP =======================
            elif self.current_screen == "TOURNAMENTS MENU":
                options = self.__menu_ui.show_tournaments_menu()

                if options == "PRINT LIST OF TOURNAMENTS":
                    self.selection_mode = "VIEW TOURNAMENTS"
                    self.current_screen = "LIST OF TOURNAMENTS"

                elif isinstance(options, tuple) and options[0] == "GET TOURNAMENT":
                    selected_tournament = options[1]
                    self.selected_tournament = selected_tournament
                    self.current_screen = "TOURNAMENT INFO MENU"
                    self.selection_mode = "SEARCH TOURNAMENT"

                elif options == "CANCEL":
                    self.current_screen = "TOURNAMENTS MENU"

                elif options == "BACK":
                    self.current_screen = "MAIN MENU"

                elif options == "QUIT":
                    break

#============================= LIST OF TOURNAMENTS MENU LOOP =======================
            elif self.current_screen == "LIST OF TOURNAMENTS":
                options = self.__menu_ui.show_view_tournaments_menu()
                
                if isinstance(options, tuple) and options[0] == "TOURNAMENT INFO":
                    selected_tournament = options[1]
                    self.selected_tournament = selected_tournament

                    if self.selection_mode == "VIEW TOURNAMENTS":
                        self.current_screen = "TOURNAMENT INFO MENU"

                    elif self.selection_mode == "ADD TEAMS":
                        self.current_screen = "ADD TEAMS TO TOURNAMENT MENU"

                    elif self.selection_mode == "GENERATE":
                        self.current_screen = "SCHEDULE GENERATION MENU"

                    elif self.selection_mode == "UPDATE":
                        self.current_screen = "TOURNAMENT UPDATE MENU"

                elif options == "BACK":
                    if self.selection_mode == "VIEW TOURNAMENTS":
                        self.current_screen = "TOURNAMENTS MENU"

                    elif self.selection_mode in ("GENERATE", "UPDATE", "ADD TEAMS"):
                        self.current_screen = "ORGANIZER MENU"
                        
                elif options == "QUIT":
                    break

#============================= TEAMS MENU LOOP =======================
            elif self.current_screen == "TEAMS MENU":
                options: str = self.__menu_ui.show_teams_menu()

                if options == "PRINT LIST OF TEAMS":
                    self.current_screen = "VIEW TEAMS MENU"
                    self.selection_mode = "VIEW TEAMS"

                elif isinstance(options, tuple) and options[0] == "GET TEAM":
                    selected_team = options[1]
                    self.selected_team = selected_team
                    self.current_screen = "TEAM INFO MENU"
                    self.selection_mode = "SEARCH TEAM"
                elif options == "CANCEL":
                    self.current_screen = "TEAMS MENU"
                elif options == "BACK":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break
            
#============================= ORGANIZER MENU LOOP =======================
            elif self.current_screen == "ORGANIZER MENU":
                options: str = self.__menu_ui.show_organizer_menu()
                if options == "CREATE TOURNAMENT":
                    self.current_screen = "TOURNAMENT CREATION MENU"

                elif options == "ADD TEAMS TO TOURNAMENT":
                    self.selection_mode =  "ADD TEAMS"
                    self.current_screen = "LIST OF TOURNAMENTS"

                elif options == "GENERATE SCHEDULE":
                    self.selection_mode = "GENERATE"
                    self.current_screen = "LIST OF TOURNAMENTS"

                elif options == "UPDATE RESULTS":
                    self.selection_mode = "UPDATE"
                    self.current_screen = "LIST OF TOURNAMENTS"

                elif options == "CANCEL":
                    self.current_screen = "ORGANIZER MENU"
                elif options == "BACK":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break

#============================= CAPTAIN HAS NO TEAM MENU LOOP =======================
            elif self.current_screen == "CAPTAIN HAS NO TEAM MENU":
                options: str = self.__menu_ui.show_captain_no_team_menu(self.captain_handle)
                if options == "CREATE TEAM":
                    self.current_screen = "CREATE TEAM MENU"
                elif options == "BACK":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break

#============================= CAPTAIN HAS TEAM MENU LOOP =======================
            elif self.current_screen == "CAPTAIN HAS TEAM MENU":
                options: str = self.__menu_ui.show_captain_has_team_menu(self.captain_handle)
                if options == "VIEW MY TEAM/PLAYERS":
                    self.current_screen = "CAPTAIN VIEW TEAM MENU"
                if options == "EDIT TEAM INFORMATION":
                    self.current_screen = "VIEW TEAM MENU"
                elif options == "BACK":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break

#============================= TOURNAMENT CREATION MENU LOOP =======================
            elif self.current_screen == "TOURNAMENT CREATION MENU":
                options: str = self.__menu_ui.show_tournament_creation_menu()
                if options == "BACK":
                    self.current_screen = "ORGANIZER MENU"
                elif options == "HOME":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break

#============================= TEAM CREATION MENU LOOP =======================
            elif self.current_screen == "CREATE TEAM MENU":
                options: str = self.__menu_ui.show_team_creation_menu(self.captain_handle)
                if isinstance(options, tuple) and options[0] == "PLAYER CREATION":
                    team = options[1]
                    self.team = team
                    self.captain_handle = options[2]
                    self.current_screen = "CREATE PLAYER MENU"
                elif options == "CANCEL":
                    self.current_screen = "CAPTAIN HAS NO TEAM MENU"
                
#============================= VIEW LIST OF TEAMS MENU LOOP =======================
            elif self.current_screen == "VIEW TEAMS MENU":
                options: str = self.__menu_ui.show_view_teams_menu()

                if isinstance(options, tuple) and options[0] == "TEAM INFO":
                    selected_team = options[1]
                    self.selected_team = selected_team
                    self.current_screen = "TEAM INFO MENU"

                elif options == "BACK":
                    self.current_screen = "TEAMS MENU"

                elif options ==  "QUIT":
                    break

#============================= VIEW TEAM INFO LOOP =======================
            elif self.current_screen == "TEAM INFO MENU":
                options: str = self.__menu_ui.show_team_info(self.selected_team)
                if options == "BACK":

                    if self.selection_mode == "SEARCH TEAM":
                        self.current_screen = "TEAMS MENU"

                    elif self.selection_mode == "VIEW TEAMS":
                        self.current_screen = "VIEW TEAMS MENU"

                elif options == "HOME":
                    self.current_screen = "MAIN MENU"
                    self.selection_mode = None

                elif options ==  "QUIT":
                    break

#============================= VIEW TOURNAMENT INFO LOOP =======================
            elif self.current_screen == "TOURNAMENT INFO MENU":
                options: str = self.__menu_ui.show_tournament_info(self.selected_tournament)
                if options == "BACK":
                    if self.selection_mode == "SEARCH TOURNAMENT":
                        self.current_screen = "TOURNAMENTS MENU"
                    elif self.selection_mode == "VIEW TOURNAMENTS":
                        self.current_screen = "LIST OF TOURNAMENTS"
                elif options == "HOME":
                    self.current_screen = "MAIN MENU"
                    self.selection_mode = None
                elif options == "QUIT":
                    break

#============================= PLAYER CREATION MENU LOOP =======================
            elif self.current_screen == "CREATE PLAYER MENU":
                options = self.__menu_ui.show_player_creation_menu(self.team, self.captain_handle)
                if options == "CONTINUE":
                    self.current_screen = "CAPTAIN HAS TEAM MENU"
                elif options == "CANCEL":
                    self.current_screen = "CAPTAIN HAS NO TEAM MENU"

#============================= ADD TEAMS TO TOURNAMENT MENU LOOP =======================
            elif self.current_screen == "ADD TEAMS TO TOURNAMENT MENU":
                options = self.__menu_ui.show_add_teams_to_tournament_menu(self.selected_tournament)
                if options == "BACK":
                    self.current_screen = "LIST OF TOURNAMENTS"
                elif options == "HOME":
                    self.current_screen = "ORGANIZER MENU"
                    self.selection_mode = None
                elif options == "QUIT":
                    break

#============================= SCHEDULE GENERATION MENU LOOP =======================
            elif self.current_screen == "SCHEDULE GENERATION MENU":
                options = self.__menu_ui.show_generate_schedule_menu(selected_tournament)
                







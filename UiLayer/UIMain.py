from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI

class UIMain:
    def __init__(self) -> None:
        logic_api = LogicAPI()
        self.__menu_ui =  MenuUI(logic_api)
        self.current_screen = "MAIN MENU"

    def mainloop(self) -> None:
        """Main loop of the menus"""
        while True:

#============================= MAIN MENU LOOP =======================
            if self.current_screen == "MAIN MENU":
                options: str = self.__menu_ui.show_main_menu()
                if options == "TOURNAMENTS":
                    self.current_screen = "LIST OF TOURNAMENTS"

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

                elif options == "QUIT":
                    break

#============================= LIST OF TOURNAMENTS PUBLIC MENU LOOP =======================
            elif self.current_screen == "LIST OF TOURNAMENTS":
                options = self.__menu_ui.show_tournaments_menu()
                if isinstance(options, tuple) and options[0] == "TOURNAMENT INFO":
                    selected_tournament = options[1]
                    self.selected_tournament = selected_tournament
                    self.current_screen = "TOURNAMENT INFO MENU"
                elif options == "BACK":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break

#============================= TEAMS MENU LOOP =======================
            elif self.current_screen == "TEAMS MENU":
                options: str = self.__menu_ui.show_teams_menu()
                if options == "PRINT LIST OF TEAMS":
                    self.current_screen = "VIEW TEAMS MENU"
                elif options == "SEARCH FOR A TEAM":
                    self.current_screen = ""
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
                    self.current_screen = "CHOOSE TOURNAMENT TO ADD TEAMS"
                elif options == "GENERATE SCHEDULE":
                    self.current_screen = "CHOOSE TOURNAMENT TO GENERATE"
                elif options == "UPDATE RESULTS":
                    self.current_screen = "CHOOSE TOURNAMENT TO UPDATE"
                elif options == "BACK":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break

#============================= CAPTAIN HAS NO TEAM MENU LOOP =======================
            elif self.current_screen == "CAPTAIN HAS NO TEAM MENU":
                options: str = self.__menu_ui.show_captain_no_team_menu(self.captain_handle)
                if options == "CREATE TEAM":
                    return "CREATE TEAM MENU"
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

#============================= TOURNAMENT CREATION MENU LOOP =======================
            elif self.current_screen == "CREATE TEAM MENU":
                options: str = self.__menu_ui.show_team_creation_menu(self.captain_handle)
                
#============================= VIEW TEAMS MENU LOOP =======================
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
                    self.current_screen = "VIEW TEAMS MENU"
                elif options == "HOME":
                    self.current_screen = "MAIN MENU"
                elif options ==  "QUIT":
                    break

#============================= VIEW TOURNAMENT INFO LOOP =======================
            elif self.current_screen == "TOURNAMENT INFO MENU":
                options: str = self.__menu_ui.show_tournament_info(self.selected_tournament)
                if options == "BACK":
                    self.current_screen = "LIST OF TOURNAMENTS"
                elif options == "HOME":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break
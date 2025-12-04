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
            if self.current_screen == "MAIN MENU":
                options: str = self.__menu_ui.show_main_menu()
                if options == "TOURNAMENTS":
                    self.current_screen = "LIST OF TOURNAMENTS"
                elif options == "TEAMS":
                    self.current_screen = "TEAMS MENU"
                elif options == "ORGANIZER":
                    self.current_screen = "ORGANIZER MENU"
                elif options == "TEAM CAPTAIN":
                    self.current_screen = "CAPTAIN MENU"
                elif options == "QUIT":
                    break


            elif self.current_screen == "TOURNAMENTS":
                ...

            elif self.current_screen == "TEAMS":
                ...
            
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

            elif self.current_screen == "TEAM CAPTAIN":
                ...

            elif self.current_screen == "TOURNAMENT CREATION MENU":
                options: str = self.__menu_ui.show_tournament_creation_menu()
                if options == "BACK":
                    self.current_screen = "ORGANIZER MENU"
                elif options == "HOME":
                    self.current_screen = "MAIN MENU"
                elif options == "QUIT":
                    break
                

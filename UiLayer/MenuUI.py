from LogicLayer.logicAPI import LogicAPI

class MenuUI:
    def __init__(self, logic_api: LogicAPI):
        self._logic_api = LogicAPI

    def __prompt_options(self, valid_options: list[str]):
        valid_lower = [i.lower() for i in valid_options]

        while True:
            choice = input("> ").strip().lower()

            if choice in valid_lower:
                return choice

            print(f"Invalid input. Valid options are: {". ".join(valid_lower)}")

    def show_main_menu(self):
        """Prints out the main menu"""
        print(
            """
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
            print(self._logic_api.showTeams(self))
            #Testing purposes#
            return "TEAMS"
        if choice == "3":
            return "ORGANIZER"
        if choice == "4":
            return "TEAM CAPTAIN"
        return "QUIT"

    def show_tournaments_menu(self):
        pass
    
    def show_teams_menu(self):
        pass

    def show_organizer_menu(self):
        pass

    def show_captain_menu(self):
        """Prints out captains menu"""
        pass

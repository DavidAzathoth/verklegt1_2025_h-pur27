from LogicLayer.logicAPI import LogicAPI


class MenuUI:
    def __init__(self, logic_api: LogicAPI):
        self._logic_api = logic_api

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
3. Login (Captain/Organizer)
q. Quit"""
        )

        choice = self.__prompt_options(["1", "2", "3", "q"])

        if choice == "1":
            return "TOURNAMENTS"
        if choice == "2":
            return "TEAMS"
        if choice == "3":
            return "LOGIN"
        return "QUIT"

from LogicLayer.logicAPI import LogicAPI
from UiLayer.BaseUI import BaseUI

class MenuUI:
    def __init__(self, logic_api: LogicAPI, base_ui: BaseUI):
        self.__logic_api = logic_api
        self.baseUI = base_ui



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

        choice = self.baseUI.prompt_options(["1", "2", "3", "4", "q"])

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
                    
                    choice = self.baseUI.prompt_options(["", "c"])
                    if choice == "":
                        continue
                    return "BACK"

                else:
                    if captain_dict.get('hasTeam').strip() == 'True':
                        captain_handle = captain_dict.get("captainHandle")
                        team = self.__logic_api.get_team_by_captain(captain_handle)
                        return ("CAPTAIN HAS TEAM", captain_handle, team)
                    else:
                        captain_handle = captain_dict.get("captainHandle")
                        return ("CAPTAIN HAS NO TEAM", captain_handle)
                    
        return "QUIT"

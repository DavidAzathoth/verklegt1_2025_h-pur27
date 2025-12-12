from Models.Team import Team
from LogicLayer.logicAPI import LogicAPI
from Models.Player import Player
import time
import sys


class BaseUI:
    def __init__(self, logic_api: LogicAPI):
        self.__logic_api = logic_api



    def prompt_options(self, valid_options: list[str]):
        """Basic prompt options"""
        valid_lower = [i.lower() for i in valid_options]

        while True:
            choice = input("> ").strip().lower()

            if choice in valid_lower:
                return choice

            print(f"Invalid input. Valid options are: {'. '.join(valid_lower)}")



    def save_player_and_team(self, player_list: list[Player], team: Team, captain_handle: str):
        """Calls LLAPI to save team and players"""
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



    def slow_print(self, text, delay = 0.04):
        """Prints a string slowly instead of instantly"""

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()



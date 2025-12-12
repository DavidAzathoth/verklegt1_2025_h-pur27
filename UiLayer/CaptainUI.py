from Models.Team import Team
from LogicLayer.logicAPI import LogicAPI
from UiLayer.selectfrompage import SelectFromPage
from UiLayer.BaseUI import BaseUI
from Models.Player import Player
from LogicLayer.menuLogic import InvalidEmailError

class CaptainUI:
    def __init__(self, logic_api: LogicAPI, base_ui: BaseUI):
        self.__logic_api = logic_api
        self.baseUI = base_ui


# CAPTAIN MENU WHEN HE HAS NO TEAM
    def show_captain_no_team_menu(self, captain_handle: str):
        """Prints out captains menu if he has no team\n
        Returns: "CREATE TEAM", "BACK", "QUIT" """

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
        
        choice = self.baseUI.prompt_options(["1", "b", "q"])

        if choice == "1":
            return "CREATE TEAM"
        if choice == "b":
            return "BACK"
        return "QUIT"


# CAPTAIN MENU WHEN HE HAS A TEAM
    def show_captain_has_team_menu(self, captain_handle: str, team: Team):
        """Prints out captain menu if has team.\n
        Return: ("VEIW MY TEAM/PLAYERS", Team), "BACK", "QUIT",  """

#========= CAPTAIN HAS TEAM MENU INTERFACE =========
        print(f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
{captain_handle}'s Menu

1. View my team/players

b. Back
q. Quit
""")
#===================================================
        
        choice = self.baseUI.prompt_options(["1", "b", "q"])
        if choice == "1":
            return ("VIEW MY TEAM/PLAYERS", team)
        if choice == "b":
            return "BACK"
        return "QUIT"


# TEAM CREATION MENU
    def show_team_creation_menu(self, captain_handle: str):
        """Prints out team creation menu where team information is given.\n
        Returns: ("PLAYER CREATION", newteam, newteam.captainHandle), "CANCEL" """

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
        choice = self.baseUI.prompt_options(["1", "2"])
        if choice == "1":
            return ("PLAYER CREATION", newteam, newteam.captainHandle)
        return "CANCEL"


# PLAYER CREATION MENU
    def show_player_creation_menu(self, team: Team, captain_handle: str):
        """Displays the player creation menu interface\n
        Returns: "CONTINUE", "CANCEL" """
        
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
            while True:
                try:
                    date_of_birth = input("Date of birth (YYYY-MM-DD): ")
                    age_check = self.__logic_api.check_player_age(date_of_birth)
                    if not age_check[0]:
                        print(age_check[1])
                        continue
                    else:
                        dob = age_check[1]
                    break
                except ValueError:
                    print("\nERROR: Invalid input. Please enter a valid date\n")
                    
            #Home address
            address = input("Player address: ").strip()

            #Phone number loop
            while True:
                try:
                    phone_num = int(input("Player phone number: ").strip())
                    break
                except ValueError:
                    print()
                    print("-" * 40)
                    print("ERROR: Please enter a valid phone number\n")

            #TeamID        
            teamID = team.teamID
            
            #Confirm player email
            while True:
                try:
                    playeremail, valid = self.__logic_api.emailVerification(input("PlayerEmail: "))
                    if valid is InvalidEmailError:
                        raise InvalidEmailError(playeremail)
                    print(("-Confirmed PlayerEmail: "), playeremail)
                    break
                
                except InvalidEmailError as playeremail:
                    print()
                    print("-" * 60)
                    print(playeremail)

            link = input("Player link: ").strip()

            #confirm player creation
            print(f"""
Create player {handle}?

1. Yes
2. Cancel                  
""")
            choice = self.baseUI.prompt_options(["1", "2"])
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
                choice = self.baseUI.prompt_options([""])
                continue
                
            elif player_count != 5: 
                print("""
1. Add another player?
2. Confirm creation
3. Cancel
""")
                choice = self.baseUI.prompt_options(["1", "2", "3"])
                if choice == "1":
                    continue

                if choice == "2":

                    self.baseUI.save_player_and_team(player_list, team, captain_handle)
                    
                    self.baseUI.prompt_options([""])
                    return  "CONTINUE"
                
                return "CANCEL"
        
        print("""
1. Confirm creation
2. Cancel              
""")
        choice = self.baseUI.prompt_options(["1", "2"]) 
        if choice == "1":
            
            self.baseUI.save_player_and_team(player_list, team, captain_handle)

            self.baseUI.prompt_options([""])
            return "CONTINUE"
        
        return "CANCEL"


# SPECIFIC PLAYER INFO MENU
    def show_player_info_menu(self, player: Player):
        """Displays options to edit specific player information.\n
        Returns: "BACK", "CAPTAIN MENU", "QUIT" """
        
        while True:
            player = self.__logic_api.getPlayer_by_gamertag(player.playerGamertag)
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
            choice = self.baseUI.prompt_options(["1", "b", "h", "q"])

            if choice == "1":
                attributes = ["address", "phoneNumber", "emailAddress", "link"]
                viewer = SelectFromPage(attributes)

                #Edit options for player
                print(f"""
------------------------------------------------
Edit player information: {player.playerGamertag}
-----------------------------------------------s-
1. Edit Address
2. Edit Phone
3. Edit Email
4. Edit Link

c. Cancel
""")
                
                edit_choice = self.baseUI.prompt_options(["1", "2", "3", "4", "c"])

                if edit_choice.isdigit():

                    num = int(edit_choice)                    
                    attribute = viewer.select_item_by_number(num)
                    
                    while True:
                        try:
                            new_value = input("""Please enter new value or press "c" (Cancel): """.strip())
                            if new_value.lower() == "c":
                                break
                            self.__logic_api.editplayer(player.playerGamertag, attribute, new_value)
                            break
                            
                        except InvalidEmailError as email:
                            print()
                            print("-" * 60)
                            print(email)  
                        
                        except ValueError:
                            print()
                            print("-" * 60)
                            print(f"ERROR: Please enter correct value for player {attribute}.\n")
                    
                    if new_value.lower() == "c":
                        continue

                    print(f"\n{attribute} has been updated!\n")
                    print("Returning to player info menu\n")
                    self.baseUI.slow_print("....", 0.4)
                    continue

                #Cancel
                continue

            if choice == "b":
                return "BACK"
                
            
            if choice == "h":
                return "CAPTAIN MENU"
            
            return "QUIT"





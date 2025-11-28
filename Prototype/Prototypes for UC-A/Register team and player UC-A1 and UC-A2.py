svar=None
login=False
num_player=1
no_team=True
while True:
    print("""
_____________________________________
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Main Menu

1. Public
2. Organizer
3. Team captain
0. Quit
          """)
    svar=int(input())
    if svar==0:
        break
    elif svar==3:
        if login==False:
            input("Team captain handle: ")
            print()
            input("Password: ")
            print()
            print("Login successful.")
            login=True
    if login==True:
        while True:
            print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Sheriff_Norris Menu

You have no current team

1. Create team
0. Back
""")
            svar=int(input())
            if svar==0:
                break
            elif svar==1:
                while True:
                    if no_team==True:
                        print("""
    ---------------------------
    RU's e-Sport Extravaganza
    ---------------------------
    Team Creation Menu
    Team captain: Sheriff_Norris

    Enter team name: Team 1
    Team website(optional): https://twitch.tv/Team-1

    1. Add new player to team
    0. Cancel
    """)
                    else:
                        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Sheriff_Norris Menu

1. View my team/players
2. Edit team information
0. Back

""")
                    svar=int(input())
                    if svar==0:
                        break
                    elif svar==1:
                        print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Add Player Menu

Add players(3-5):""")
                        add_player=True
                        while True:
                            if add_player==True:
                                print(f"Add player {num_player}")
                                input("Handle: ")
                                input("Name: ")
                                input("Date of birth(YYYY-MM-DD): ")
                                input("Address: ")
                                input("Phone number: ")
                                input("E-mail: ")
                                input("Link: ")
                                print()
                                print("Player has been added to team!")
                                num_player+=1
                                if num_player>3:
                                    print('1. Add another player(max 5)')
                                    print("2. Confirm creation")
                                    print("0. Cancel")
                                    print()
                                    svar=int(input())
                                    if svar==0:
                                        add_player=False
                                    elif svar==2:
                                        add_player=False
                            else:
                                        print("""
    ---------------------------
    RU's e-Sport Extravaganza
    ---------------------------
    Team "Team 1" has been successfully created.
    Team captain: Sheriff_Norris 

    1. Continue""")
                                        svar=int(input())
                                        if svar==1:
                                            no_team=False
                                            break
                                



#Add Player 1:
#Handle: Sheriff_Norris
#Name: Chuck
#Date of birth(YYYY-MM-DD): 1940-03-10
#Address: 872 Navasota TX
#Phone number: +44 207 234 9455
#E-mail: gmail@chucknorris.com
#Link: https://www.facebook.com/share/1CxgXUzHaw/?mibextid=wwXIfr






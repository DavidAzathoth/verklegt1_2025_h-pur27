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
Team captain Edit team members
---------------------------
RU's e-Sport Extravaganza
---------------------------
Sheriff_Norris Men
1. View my team/players
2. Edit team information
0. Back
""")
            svar=int(input())
            if svar==0:
                break
            elif svar==1:
                while True:
                    print("""
---------------------------
RU's e-Sport Extravaganza
---------------------------
View Team Men
Team name: Team 1
Players:
1. Sheriff_Norris
2. Player_A
3. Player_B
4. Player_C
5. Player_D
0. Back
""")
                    svar=int(input("Select player (1-5) or 0 to go back: "))
                    if svar==0:
                        break
                    elif svar==2:
                        while True:
                            print("""
---------------------------
RU's e-Sport Extravaganza
---------------------------
Player_A personal info
Handle: Player_A
Name: Bob
Date of birth(YYYY-MM-DD): 2002-04-09
Address: somestreetname 12
Phone number: 980-4321
E-mail: playera@gmail.com
Link: https://www.twitch.tv/Player-A
1. Edit player info
0. Back
""")
                            svar=int(input())
                            if svar==0:
                                break
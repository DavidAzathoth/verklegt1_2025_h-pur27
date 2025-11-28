svar=None
login=False
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
    elif svar==2:
        if login==False:
            input("Password: ")
            print()
            print("Password has been verified.")
            login=True
    if login==True:
        while True:
            print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Organizer Menu

1. Create tournament
2. Add teams to tournament
3. Generate schedule
4. Update results
5. View teams/players
0. Back
""")
            svar=int(input())
            if svar==0:
                break
            elif svar==5:
                while True:
                    print("""
---------------------------
RU's e-Sport Extravaganza
---------------------------
View Teams
Teams:
1. Team_1
2. Team_2
3. Team_3
4. Team_4
5. Team_5
0. Back
""")
                    svar=int(input("Select team to view: "))
                    if svar==0:
                        break
                    elif svar==1:
                        while True:
                            print("""
---------------------------
RU's e-Sport Extravaganza
---------------------------
View Team
Team name: Team 1
Players:
1. Sheriff_Norris
2. Player_A
3. Player_B
4. Player_C
5. Player_D
0. Back""")
                            svar=int(input())
                            if svar==0:
                                break
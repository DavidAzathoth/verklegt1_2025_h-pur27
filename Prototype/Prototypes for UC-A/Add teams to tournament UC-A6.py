login=False
svar=None
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
            ret_to_menu=False
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
            elif svar==2:
                while True:
                    if ret_to_menu==True:
                        break
                    print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Choose Tournament

1. HA cup finals
2. HRingurinn
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
Add Teams To Tournament: HA cup final

Teams currently registered:
- Team 1
- Team 3

Available teams:
1. Team 2
2. Team 4
3. Team 5
4. Team 6
0. Back
""")
                            svar=int(input("Select team to add: "))
                            if svar==0:
                                break
                            elif svar==1:
                                print("""
------------------------------------------------
Team "Team 2" has been added to HA cup final

Current number of teams: 3
NOTE: minimum amount required: 16 teams

1. Add another team
2. Finish and go back to organizer menu
""")
                                svar=int(input())
                                if svar==2:
                                    useless_variable=True
                                    ret_to_menu=True
                                    break
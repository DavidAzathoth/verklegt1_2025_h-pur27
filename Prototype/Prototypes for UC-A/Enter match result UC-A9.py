login=False
svar=None
add_match=False
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
            elif svar==4:
                while True:
                    if ret_to_menu==True:
                        break
                    print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Choose tournament to update results

1. HA cup final
2. HRingurinn
0. Back
""")
                    svar=int(input())
                    if svar==0:
                        break
                    elif svar==1:
                        while True:
                            if ret_to_menu==True:
                                break
                            print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Update results: HA cup final

1. View completed matches
2. View unfinished matches
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
Unfinished matches

1. Match 1A   Team 1 vs Team 2
2. Match 1B   Team 4 vs Team 6
3. Match 2A   Team 15 vs Team 3
0. Back
""")
                                    svar=int(input("Select a match to update: "))
                                    if svar==0:
                                        break
                                    elif svar==2:
                                        while True:
                                            if ret_to_menu==True:
                                                break
                                            if add_match==True:
                                                add_match=False
                                                break
                                            add_match=False
                                            print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Update results from match

Match: 1B
Teams: Team 4 vs Team 6
Date:  2025-11-28 18:00
Server: 2
Status: Waiting for results
""")
                                            while True:
                                                try:
                                                    score=int(input("Enter Team 4 score: "))
                                                    score=int(input("Enter Team 6 score: "))
                                                    break
                                                except:
                                                    print("ERROR: Invalid input. Please enter a valid number.")
                                                    continue
                                            print("""
Winner confirmation: Team 4

1. Confirm results
2. Re-enter results
3. Cancel
""")
                                            svar=int(input())
                                            if svar==3:
                                                break
                                            elif svar==1:
                                                print("""
------------------------------------------
Results have been confirmed and moved to "complete matches"

Future rounds will be updated accordingly
""")
                                                while True:
                                                    print("""
1. Update another match
2. Back to Organizer menu
""")
                                                    svar=int(input())
                                                    if svar==1:
                                                        add_match=True
                                                        break
                                                    elif svar==2:
                                                        ret_to_menu=True
                                                        break
                                                        
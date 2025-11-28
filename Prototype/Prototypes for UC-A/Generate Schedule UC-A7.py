import time
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
            elif svar==3:
                while True:
                    if ret_to_menu==True:
                        break
                    print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Choose tournament to generate schedule
Showing teams 1-8
                          
Current number of teams: 16
                          
1. HA cup final
2. HRingurinn
3. Astralis
4. fnatic
5. Heroic
6. Outsiders
7. MOUZ
8. Ninjas in Pyjamas
9. Show next page

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
""")
                            print("Generaterating schedule.",end='\r')
                            time.sleep(1)
                            print("Generaterating schedule..",end='\r')
                            time.sleep(1)
                            print("Generaterating schedule...",end='\r')
                            time.sleep(1)
                            print("Schedule has been generated.")
                            print()
                            print("""
This is the schedule for: HA cup final


First rounds:
Match 1A: Team 1 vs Team 2      Date: 2025-11-28  18:00    Server: 1
Match 1B: Team 4 vs Team 6      Date: 2025-11-28  18:00    Server: 2
Match 2A: Team 15 vs Team 3     Date: 2025-11-28  19:00    Server: 1
Match 2B: Team 8 vs Team 10     Date: 2025-11-28  19:00    Server: 2
...

NOTE: Quarterfinals, semifinals and finals will be determined as results are updated

1. Go back to organizer menu""")
                            svar=int(input())
                            if svar==1:
                                ret_to_menu=True
                                break



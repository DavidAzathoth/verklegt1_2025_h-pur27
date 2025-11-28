while True:
    print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Main menu

1. Public
2. Organizer
3. Team captain
0. Quit
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
Public menu

1. View tournaments
2. View teams/players
0. Back
""")
            svar=int(input())
            if svar==0:
                break
            elif svar==2:
                while True:
                    print("""
---------------------------
RU's e-sport extravaganza 
---------------------------
Teams menu
1. Print list of teams
2. Search for team
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
View teams

1. Team 1
2. Team 2
3. Team 3
4. Team 4
                                  
0. Back
                                  
""")
                            svar=input("Enter team name: ")
                            try:
                                nextpage=False
                                num_svar=int(svar)
                                if num_svar==0:
                                    break
                                if num_svar==1:
                                    nextpage=True
                            except:
                                    if svar=="Team 1":
                                        nextpage=True
                            if nextpage:
                                    while True:
                                        print("""
---------------------------
 RU's e-Sport extravaganza
---------------------------
View team
Name: Team 1
Captain: Captain_1
Player handles:
player_A
player_B
player_C
player_D
Tournaments:
HA cup finals
                                              
0. Back
""")
                                        svar=int(input())
                                        if svar==0:
                                            break
                     
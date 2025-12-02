while True:
      print("""
__________________________________________________
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
                  if svar==1:
                        while True:
                              print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
List of tournaments

1. Ha cup Final
2. HRingurinn
0. Back""")
                              svar=int(input("Select tournament: "))
                              if svar==0:
                                    break
                              if svar==1:
                                    while True:
                                          print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Name: HA Cup Final
Venue: HA
start date: 28. nov
End date: 30. nov

1. View schedule
2. View results/standings
0. Back""")
                                          svar=int(input())
                                          if svar==0:
                                                break
                                          elif svar==1:
                                                while True:
                                                      print("""
--------------------------- 
 RU's e-sport extravaganza
---------------------------
Match Schedule

Match number: 1A
Team 1 vs Team 2
Date: 28. nov, 21:00
Server: 1

Match number: 1B
Team 3 vs team 4
date: 28. nov, 21:00
Server 2
                                                            
0. Back
""")
                                                      svar=int(input())
                                                      if svar==0:
                                                            break
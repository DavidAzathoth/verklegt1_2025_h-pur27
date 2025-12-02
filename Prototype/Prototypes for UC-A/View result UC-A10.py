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
                                          elif svar==2:
                                                print("""
---------------------------
 RU's e-sport extravaganza
---------------------------
Tournament results and standings
HA cup final

View completed matches
2. View unfinished matches
3. View full standings
0. Back
""")
                                                svar=int(input())
                                                if svar==0:
                                                      break
                                                elif svar==3:
                                                      print("""
Public View Standings
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Full Standings — HA Cup Final

Progress:
- First rounds: 8 / 8 matches played
- Quarterfinals: 2 / 4 matches played
- Semifinals: Not started
- Final: Not started

------------------------
Rankings
------------------------

First rounds (Completed)
---------------------------
Match 1A: Team 1  vs Team 16    (Winner: Team 1)
Match 1B: Team 8  vs Team 9     (Winner: Team 8)
Match 1C: Team 4  vs Team 13    (Winner: Team 4)
Match 1D: Team 6  vs Team 11    (Winner: Team 6)
Match 1E: Team 2  vs Team 15    (Winner: Team 2)
Match 1F: Team 10 vs Team 7     (Winner: Team 10)
Match 1G: Team 3  vs Team 14    (Winner: Team 3)
Match 1H: Team 5  vs Team 12    (Winner: Team 5)

Teams eliminated:
- Team 16, Team 9, Team 13, Team 11
- Team 15, Team 7, Team 14, Team 12


---------------------------
Quarterfinals (In Progress)
---------------------------

Match Q1: Team 1 vs Team 8          (Completed)
Winner: Team 8

Match Q2: Team 4 vs Team 6          (Completed)
Winner: Team 6

Match Q3: Team 2 vs Team 10         (Pending)
Match Q4: Team 3 vs Team 5          (Pending)


---------------------------
Semifinals (Not Yet Started)
---------------------------



---------------------------
Final (Not Yet Started)
---------------------------
""")
                                                      svar=int(input())
                                                      if svar==0:
                                                            break
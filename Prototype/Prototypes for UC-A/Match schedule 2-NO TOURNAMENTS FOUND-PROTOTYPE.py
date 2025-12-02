svar=None
while True:
      print("""
Public Match schedule
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
      if svar==1:
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
Error no tournaments found

---------------------------
 RU's e-Sport Extravaganza
---------------------------
List of tournaments

No tournaments found.

0. Back""")
                              svar=int(input())
                              if svar==0:
                                    break

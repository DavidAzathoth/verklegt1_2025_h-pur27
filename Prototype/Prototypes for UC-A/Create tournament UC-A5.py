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
            elif svar==1:
                while True:
                    print("""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
Tournament Creation Menu
""")
                    input("Enter venue location: ")
                    input("Enter tournament name: ")
                    print()
                    input("Enter start date (YYYY-MM-DD): ")
                    input("Enter end date(YYYY-MM-DD): ")
                    print()
                    input("Enter contact person's email: ")
                    input("Enter contact person's phone number: ")
                    print()
                    print("""
1. Confirm creation
2. Cancel
""")
                    svar=int(input())
                    if svar==2:
                        break
                    elif svar==1:
                        print("""
---------------------------------------------------
Tournament has successfully been created!

1. Back to organizer menu
""")
                        svar=int(input())
                        if svar==1:
                            break
class ShowTeams:
    def __init__(self,teams):
        self.teams=teams
        self.page=1
        pass
    def __str__(self):
        return (f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
View teams
              
{self.teams}
""")
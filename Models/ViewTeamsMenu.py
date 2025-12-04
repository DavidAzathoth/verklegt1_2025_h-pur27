class ShowTeams:
    def __init__(self,teams):
        self.teams=teams
        self.teamslist=self.teams.split('\n')
        self.endpage=5
        self.startpage=0
        pass
    def __str__(self):
        return (f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
View teams
              
{self.nextPage()}
""")
    def nextPage(self):
        page=self.teamslist[self.startpage:self.endpage]
        page=('\n').join(page)
        return page
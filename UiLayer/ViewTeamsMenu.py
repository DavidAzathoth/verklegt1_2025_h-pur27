class ShowTeams:
    def __init__(self,teams):
        self.teams=teams
        self.endpage=5
        self.startpage=0
        pass

    def __str__(self):
        return (f"""
---------------------------
 RU's e-Sport Extravaganza
---------------------------
View teams menu
              
{self.nextPage()}
""")
    
    def nextPage(self):
        teams_list: list=self.teams[self.startpage:self.endpage]
        page = []
        for num in range(len(teams_list)):
            page.append(f'{num+1}. {teams_list[num]}')
        page=('\n').join(page)
        return page
    
    def next_page(self):
        self.startpage+=5
        self.endpage+=5

        if self.startpage >= len(self.teams):
            self.startpage = 0
            self.endpage = 5

    def get_team_by_number(self, number: int) -> str | None:
        teams_list: list = self.teams[self.startpage:self.endpage]
        if 1 <= number <= len(teams_list):
            return teams_list[number - 1]
        return None
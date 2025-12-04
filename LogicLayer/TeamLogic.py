from StorageLayer.storageApi import DataAPI
from Models.Team import Team

class Teamlogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass
    
    def getTeams(self) -> list[Team]:
        raw_list = self.__dataApi.loadTeams()

        if not raw_list:
            return []
        
        teams = []

        for row in raw_list:
            team = Team(
                teamID = row["teamID"],
                teamName = row["teamName"],
                roster = row["roster"],
                wins = int(row["wins"]) if row["wins"] else 0,
                losses = int(row["losses"]) if row["losses"] else 0,
                captainHandle = row["captainHandle"]
            )
            teams.append(team)
        return teams

    def get_team_by_captain(self, captain_handle: str):
        teams = self.getTeams()
        for team in teams:
            if team.get("captainHandle") == captain_handle:
                return team
        return None
    
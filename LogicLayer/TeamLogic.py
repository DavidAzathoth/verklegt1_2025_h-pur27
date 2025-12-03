from StorageLayer.storageApi import DataAPI
from Models.Team import Team

class Teamlogic:
    def __init__(self, dataApi: DataAPI):
        self.__dataApi = dataApi
        pass
    
    def getTeams(self) -> list[Team]:
        return self.__dataApi.loadTeams()

    def get_team_by_captain(self, captain_handle: str) -> Team | None:
        teams = self.getTeams()
        for team in teams:
            if team.get("captainHandle") == captain_handle:
                return team
        return None
    
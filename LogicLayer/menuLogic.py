from LogicLayer.TeamLogic import Teamlogic
from StorageLayer.storageApi import DataAPI
class MenuLogic:
    def __init__(self,dataApi: DataAPI):
        self.__dataApi = dataApi
        self.__teamlogic: Teamlogic = Teamlogic(self.__dataApi)
        pass
    def createTeamsString(self):
        teamslist: list = self.__teamlogic.getTeams()
        ()
        teamnames=[]
        for teamslist in teamslist:
            teamnames.append(teamslist.get('teamName'))
        teamString="\n".join(teamnames)
        return teamString

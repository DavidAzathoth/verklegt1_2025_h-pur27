
from roughtest.StorageLayer.StorageAPI import StorageManager

class LogicAPI:
    def __init__(self):
        pass

    def findteam(self,requested_team: str):
        ioapi=StorageManager()
        teams=ioapi.loadTeams()
        for team in teams:
            if team.get('teamName')==requested_team:
                found_team=team.get('teamName')
                players=team.get('roster').split(',')
        ret_string=(f"""
{'-'*len(found_team)}
{found_team}
{'-'*len(found_team)}
""")
        for player in players:
            ret_string+=(f"{player}\n")
        return ret_string
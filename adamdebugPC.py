from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI
from StorageLayer.storageHandler import StorageHandler
from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from Models.Player import Player
from StorageLayer.storageApi import DataAPI
from Models.ViewTeamsMenu import ShowTeams
da=DataAPI()
streg=''
teams=da.loadTeams()
tostring=[]
print(teams)
if teams:
    teamlist=[]
    for team in teams:
        teamid=team.get('teamID')
        teamname=team.get('teamName')
        roster=team.get('roster')
        wins=team.get('wins')
        losses=team.get('losses')
        teamlist.append(Team(teamid,teamname,roster,wins,losses,None))
    for team in teamlist:
        tostring.append(team.createCSVString())

else:
    print('File not found')
print(f"Invalid input. Valid options are: {". ".join(valid_lower)}")


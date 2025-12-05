#from UiLayer.MenuUI import MenuUI

from LogicLayer.logicAPI import LogicAPI
from LogicLayer.PlayerLogic import Playerlogic
#from StorageLayer.storageHandler import StorageHandler
#from Models.Team import Team
#from Models.TeamCaptain import TeamCaptain
#from Models.Player import Player
from StorageLayer.storageApi import DataAPI
#from Models.ViewTeamsMenu import ShowTeams

da = DataAPI()
llapi=LogicAPI()
pllogic = Playerlogic(da)
inputlisti=['1','2','3',4,5,'6']
#print(llapi.createteam(inputlisti).createCSVDict())
teams=llapi.getTeams()
team=teams[1]
print(team.playerinstances)
for player in team.playerinstances:
    print(player.teamID)
print(team.roster)
#teams=llapi.getTeams()
#for team in teams:
#    print(team.teamID)
#testlist=['1','2','3','4','5','6','dontforgetaboutme','lol']
#p1=pllogic.createplayer(testlist)
#pllogic.saveplayer(p1)
#print(pllogic.loadplayers())


#tournaments = logic.gettournament()
#print(tournaments)
#teams = logic.showTeams()
#print(teams)
#MenuUI(logic).show_main_menu()

#listi = input("tournament info")
#minnlisti = listi.split()
#LogicAPI.createTournament(minnlisti)

        #self.teamID: str = teamID
        #self.teamName: str = teamName
        #self.roster: list = roster.split(',')
        #self.wins: int = wins
        #self.losses: int = losses
        #self.captainHandle: str = captainHandle

#testlist=[{'name':'alfred','age':'52','height':'192cm'},{'name':'bob','age':'33','height':'183cm'}]
#templist=testlist
#for person in testlist:
    #if person.get('name')=='alfred':
        #index=testlist.index(person)
        #person_edited=person
        #person_edited['age']=56
#testlist.pop(index)
#testlist.insert(index,person_edited)
#print(testlist)

#captainHandle,hasTeam
#Sheriff_Norris,False

#team = input("enter team info")
#teams = team.split()
#logic.createteam(teams)

#cap = input("Captain Handle")
#logic.updatecaptain(cap)
#def printnumbers(a,b,c,d,e,f):
#    print(f,e,d,c,b,a)
#listi=[1,2,3,4,5,6]
#printnumbers(*listi)
from UiLayer.MenuUI import MenuUI
from LogicLayer.logicAPI import LogicAPI
from StorageLayer.storageHandler import StorageHandler
from Models.Team import Team
from Models.TeamCaptain import TeamCaptain
from Models.Player import Player
from StorageLayer.storageApi import DataAPI
from Models.ViewTeamsMenu import ShowTeams

da = DataAPI()
logic = LogicAPI()
tournaments = logic.gettournament()
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
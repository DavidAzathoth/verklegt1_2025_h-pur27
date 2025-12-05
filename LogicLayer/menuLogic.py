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

    def emailVerification(self, email):
        atcount=0
        atposition=None
        extradotpos=None
        cons_dots=False
        cons_dots_pos=None
        allgood=True
        #print(email.find('a'))
        for i, x in enumerate(email):
            if '@'==x and atcount>0:
                return f"{email}\n{' ' * i}^--there is an extra @ symbol here."

            if '@'==x:
                atcount+=1
                atposition=i
                #print('-'i+'^')
            if '.'==x:
                if email[i+1]=='@':
                    extradotpos=i
                if email[i+1]=='.':
                    cons_dots_pos=i
                    cons_dots=True

        if allgood==True:
            if email.find('@') ==0:
                return 'There is nothing before the @ symbol.'
            elif atcount==0:
                return '@ symbol is missing.'
            elif email[::-1].find('@')==0:
                return f"{email}\n{' ' * (atposition+1)}^--there is nothing after the @ symbol."
            elif email.find('.')==0:
                return 'Email address starts with a dot.'
            elif bool(email.find('.@') + 1)==True:
                return f"{email}\n{' ' * extradotpos}^--there is an extra dot here."
            elif cons_dots==True:
                return f"{email}\n{' ' * cons_dots_pos}^--there are consecutive dots here."
            elif email[::-1].find('@')<email[::-1].find('.') or email.find('.')==-1:
                return 'Top-level-domain is missing.'
            elif allgood==True:
                return 'All good.'
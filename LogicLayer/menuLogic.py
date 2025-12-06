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

    def emailverification(self, email: str):
        ret_string = ""
        allgood = True
        atcount=0
        atposition=None
        extradotpos=None
        cons_dots=False
        cons_dots_pos=None
        #print(email.find('a'))
        for i, x in enumerate(email):
            if '@'==x and atcount>0:
                ret_string = f"{email}\n{' ' * i}^--there is an extra @ symbol here."
                allgood=False

            if '@'==x:
                atcount+=1
                atposition=i
                #print('-'*i+'^')
            if '.'==x:
                if email[i+1]=='@':
                    extradotpos=i
                if email[i+1]=='.':
                    cons_dots_pos=i
                    cons_dots=True

 
        if email.find('@') ==0:
            ret_string='There is nothing before the @ symbol.'
            allgood=False
        elif atcount==0 and allgood:
            ret_string = '@ symbol is missing.'
            allgood=False
        elif email[::-1].find('@')==0 and allgood:
            ret_string = f"{email}\n{' ' * (atposition+1)}^--there is nothing after the @ symbol."
            allgood=False
        elif email.find('.')==0 and allgood:
            ret_string = 'Email address starts with a dot.'
            allgood=False
        elif bool(email.find('.@')+1)==True and allgood:
            ret_string = f"{email}\n{' ' * extradotpos}^--there is an extra dot here."
            allgood=False
        elif cons_dots==True and allgood:
            ret_string = f"{email}\n{' ' * cons_dots_pos}^--there are consecutive dots here."
            allgood=False
        elif email[::-1].find('@')<email[::-1].find('.') or email.find('.')==-1 and allgood:
            ret_string: str = 'Top-level-domain is missing.'
            allgood=False
        if allgood:
            ret_string=email
        return (ret_string, allgood)

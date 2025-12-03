class Tournament:
    def __init__(self, venue: str, name: str, startDate: str, endDate: str, contactEmail: str, contactPhone: str, matchesList: list = [], matchHistory: list = [], teams: list = [], active: bool = True):
        self.contactEmail = contactEmail
        self.contactPhone = contactPhone
        self.venue = venue
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.matchesList = matchesList
        self.matchHistory = matchHistory
        self.teams = teams
        self.active = active
    
    def createCSVString(self):
        ret_str: str = f'{self.venue},{self.name},{self.startDate},{self.endDate},{self.contactEmail},{self.contactPhone},"{','.join(self.matchesList)}","{','.join(self.matchHistory)}","{','.join(self.teams)}",{self.active}'
        return ret_str
    def createCSVDict(self)-> dict:
        """Creates a dictionary to store in a csv file"""
        ret_dic={'venue':self.venue,'name':self.name,'startDate':self.startDate,'endDate':self.endDate,'contactEmail':self.contactEmail,'contactPhone':self.contactPhone,'matchesList':",".join(self.matchesList),'matchHistory':",".join(self.matchHistory),'teams':",".join(self.teams),'active':self.active}
        return ret_dic
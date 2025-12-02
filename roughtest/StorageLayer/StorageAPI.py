import csv
class StorageManager:
    def __init__(self):
        self.teamsfilepath="StorageLayer/Data/teams.csv"
    def loadTeams(self) -> list:
        with open(self.teamsfilepath,'r') as file:
            teams=[]
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                teams.append(row)
        file.close()
        return teams
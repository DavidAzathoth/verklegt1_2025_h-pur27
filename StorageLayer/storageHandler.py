import csv
class StorageHandler:
    def __init__(self):
        pass
    def retrieveFile(self,file: str,type: str = None) -> list[type]:
        ret_list=[]
        try:
            with open(file,'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    ret_list.append(row)
            file.close()
        except FileNotFoundError:
            return False
        return ret_list
    def saveFile(self, addition, type):
        if type=='teams':
            loaded=self.retrieveFile('StorageLayer/Data/teams.csv')
            try:
                with open('StorageLayer/Data/teams.csv','w') as file:
                    keys = loaded[0].keys()
                    csvwriter=csv.DictWriter(file, keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(loaded)
                    csvwriter.writerow(addition)
                
            except FileNotFoundError:
                return False
        if type=='tournaments':
            pass
        pass
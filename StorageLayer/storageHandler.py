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
            retr_file='StorageLayer/Data/teams.csv'
            ##
            loaded=self.retrieveFile(retr_file)
            
            
        if type=='tournaments':
            retr_file='StorageLayer/Data/tournaments.csv'
            loaded=self.retrieveFile('StorageLayer/Data/tournaments.csv')
            
        try:
            with open(retr_file,'r') as file: #We need to open the file first to get fieldnames for the DictReader
                csvreader=csv.DictReader(file)
                keys=csvreader.fieldnames
            file.close()
            with open(retr_file,'w') as file:
                csvwriter=csv.DictWriter(file, keys)
                csvwriter.writeheader()
                csvwriter.writerows(loaded)
                csvwriter.writerow(addition)
            file.close()
        except FileNotFoundError:
            return False
   #def editFile(self, addition, removal, type):
   #    if 
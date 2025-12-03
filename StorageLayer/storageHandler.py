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
            loaded=self.retrieveFile('StorageLayer/Data/testfile.csv')
            try:
                with open('StorageLayer/Data/testfile.csv','r') as file: #We need to open the file first to get fieldnames for the DictReader
                    csvreader=csv.DictReader(file)
                    keys=csvreader.fieldnames
                file.close()
                with open('StorageLayer/Data/testfile.csv','w') as file:
                    csvwriter=csv.DictWriter(file, keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(loaded)
                    csvwriter.writerow(addition)
                file.close()
            except FileNotFoundError:
                return False
            
        if type=='tournaments':
            loaded=self.retrieveFile('StorageLayer/Data/tournaments.csv')
            try:
                with open('StorageLayer/Data/tournaments.csv','r') as file:
                    csvreader=csv.DictReader(file)
                    keys=csvreader.fieldnames
                file.close()
                with open('StorageLayer/Data/tournaments.csv','w') as file:
                    csvwriter=csv.DictWriter(file, keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(loaded)
                    csvwriter.writerow(addition)
                file.close()
            except FileNotFoundError:
                return False
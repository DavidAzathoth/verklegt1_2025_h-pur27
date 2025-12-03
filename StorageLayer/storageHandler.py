import csv
class StorageHandler:
    def __init__(self):
        pass
    def retrieveFile(self,file: str,type: str = None) -> list[type]:
        ret_list=[]
        try:
            with open(file,'r') as file:
                csv_reader = csv.DictReader(file)
                test=csv_reader.fieldnames
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
                with open('StorageLayer/Data/testfile.csv','r') as file:
                    csvreader=csv.DictReader(file)
                    keys=csvreader.fieldnames
                file.close()
                with open('StorageLayer/Data/testfile.csv','w') as file:
                    #keys = loaded[0].keys()
                    csvwriter=csv.DictWriter(file, keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(loaded)
                    csvwriter.writerow(addition)
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
                    #keys = csv.DictReader(file).fieldnames()
                    csvwriter=csv.DictWriter(file, keys)
                    csvwriter.writeheader()
                    csvwriter.writerows(loaded)
                    csvwriter.writerow(addition)
            except FileNotFoundError:
                return False
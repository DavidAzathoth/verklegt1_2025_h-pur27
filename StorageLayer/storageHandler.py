import csv
from datetime import datetime
class StorageHandler:
    def __init__(self):
        pass
    def retrieveFile(self,file: str) -> list[type]:
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


    def saveFile(self,file,data):
        try:
            with open(file,'r') as fileT: #We need to open the file first to get fieldnames for the DictReader
                csvreader=csv.DictReader(fileT)
                keys=csvreader.fieldnames
            fileT.close()

            loaded=self.retrieveFile(file)
            self.createBackup(file,loaded,keys)
            loaded.append(data)
            with open(file,'w',newline='') as fileT:
                csvwriter=csv.DictWriter(fileT, keys)
                csvwriter.writeheader()
                csvwriter.writerows(loaded)
            fileT.close()

        except FileNotFoundError:
            return False
        return
    
    def createBackup(self,file,backup,keys):
        date=datetime.today().strftime('%Y-%m-%d-%H-%M')
        suffix=file.removeprefix('StorageLayer/Data/')
        datatype=suffix.removesuffix('.csv')
        file='StorageLayer/Data/Backup/'+datatype+date+'.csv'
        with open(file,'w',newline='')as file:
            csvwriter=csv.DictWriter(file,keys)
            csvwriter.writeheader()
            csvwriter.writerows(backup)
        file.close()

    def editFile(self,file,data):
        try:
            with open(file,'r') as fileT: #We need to open the file first to get fieldnames for the DictReader
                csvreader=csv.DictReader(fileT)
                keys=csvreader.fieldnames
            fileT.close()

            loaded=self.retrieveFile(file)
            self.createBackup(file,loaded,keys)
            with open(file,'w',newline='') as fileT:
                csvwriter=csv.DictWriter(fileT, keys)
                csvwriter.writeheader()
                csvwriter.writerows(data)
            fileT.close()

        except FileNotFoundError:
            return False
        return
    
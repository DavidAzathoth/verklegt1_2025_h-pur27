import csv
from datetime import datetime
import os
class StorageHandler:
    def __init__(self):
        pass
    def retrieveFile(self,file: str) -> list[type]:
        ret_list=[]
        try:
            with open(file,'r', encoding='utf-8-sig') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    ret_list.append(row)
            file.close()
        except FileNotFoundError:
            return False
        return ret_list


    def saveFile(self,file,data):
        try:
            with open(file,'r', encoding='utf-8-sig') as fileT: #We need to open the file first to get fieldnames for the DictReader
                csvreader=csv.DictReader(fileT)
                keys = csvreader.fieldnames
            fileT.close()

            loaded = self.retrieveFile(file)

            self.createBackup(file,loaded,keys)
            loaded.append(data)
            with open(file,'w',newline='', encoding='utf-8-sig' ) as fileT:
                csvwriter=csv.DictWriter(fileT, keys)
                csvwriter.writeheader()
                csvwriter.writerows(loaded)
            fileT.close()

        except FileNotFoundError:
            return False
        return
    
    def createBackup(self,file,backup,keys): 
        date=datetime.today().strftime('%Y-%m-%d-%H-%M') #Creates a string with current time
        suffix=file.removeprefix('StorageLayer/Data/')
        datatype=suffix.removesuffix('.csv')
        file='StorageLayer/Data/Backup/'+datatype+date+'.csv' 
        with open(file,'w',newline='', encoding='utf-8-sig')as file:
            csvwriter=csv.DictWriter(file,keys)
            csvwriter.writeheader()
            csvwriter.writerows(backup)
            
        file.close()

    def editFile(self,file,data):
        try:
            with open(file,'r', encoding='utf-8-sig') as fileT:
                csvreader=csv.DictReader(fileT)
                keys=csvreader.fieldnames
            fileT.close()

            loaded=self.retrieveFile(file)
            self.createBackup(file,loaded,keys)
            with open(file,'w',newline='', encoding='utf-8-sig') as fileT:
                csvwriter=csv.DictWriter(fileT, keys)
                csvwriter.writeheader()
                csvwriter.writerows(data)
            fileT.close()

        except FileNotFoundError:
            return False
        return
    def cleanBackups(self):
        path = 'StorageLayer/Data/Backup'
        for entry in os.scandir(path):
            print(entry.path)
            if entry.path == 'StorageLayer/Data/Backup\dontdelete.txt':
                pass
            else:
                os.remove(entry.path)
            
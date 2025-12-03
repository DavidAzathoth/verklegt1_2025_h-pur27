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
    def saveFile(self, csvfile: str, type: str = None):
        if type=='teams':
            csvfile="teamID,teamName,roster,wins,losses,captainhandle"+csvfile
            try:
                with open('StorageLayer/Data/testfile.csv','w') as file:
                    csv.writer=file
                
            except FileNotFoundError:
                return False
                    
        pass
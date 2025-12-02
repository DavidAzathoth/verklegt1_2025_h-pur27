import csv
class StorageHandler:
    def __init__(self):
        pass
    def retrieveFile(self,file: str,type: str = None) -> list[type]:
        ret_list=[]
        with open(file,'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                ret_list.append(row)
        file.close()
        return ret_list
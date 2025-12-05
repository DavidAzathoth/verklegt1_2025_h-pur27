class logicHandler:
    def __init__(self):
        pass
    def createModel(self,model,data: list):
        return model(*data)
    
    def loadmodels(self,model,data):
        itemlist=[]
        for item in data:
            values=item.values()
            iteminstance=self.createModel(model,values)
            itemlist.append(iteminstance)
        return itemlist
    
        
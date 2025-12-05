class logicHandler:
    def __init__(self):
        pass
    def createModel(self,model: object,data: list):
        return model(*data)
    
    def loadmodels(self,model: object,data):
        itemlist=[]
        for item in data:
            values=item.values()
            iteminstance=self.createModel(model,values)
            itemlist.append(iteminstance)
        return itemlist
    
        
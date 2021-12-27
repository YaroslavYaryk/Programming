class Mine(list):

    def __init__(self):
        self._storage = []

    def __str__(self):
        return f"{self._storage}"    


obj = Mine()
obj.append(5)        
obj.append(5)        
obj.append(5)        
print(obj)
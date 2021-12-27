


class Counter():

    def __init__(self, text):
        self.__counter = {}
        self.__text = text
        self.make_operation()
        
    def make_operation(self):
        for elem in self.__text:
            if elem not in self.__counter:
                self.__counter[elem] = 1
            else:
                self.__counter[elem] +=1
                
                
    def __repr__(self):
        return  f'Counter({self.__counter})' 
    
    
    def __iter__(self):
        for elem in self.__counter:
            yield elem
            
    def __getitem__(self, index):
        try:
            return self.__counter[index]
        except IndexError:
            return "Can't handle it"
        
    def __len__(self):
        return len(self.__counter)
        
            
                
                        
        
a = Counter("hello world")
a["l"] = 5
print(a["l"])     

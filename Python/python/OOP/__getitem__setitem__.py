class Figures(object):

    __slots__ = ("values") 

    def __init__(self, *args):
        self.values = list(args)


    def __getitem__(self, key):
        if 0<key<len(self.values):
            return self.values[key]
        else:
            raise IndexError("index out of range")


    def __setitem__(self, key, value):
        if 0<key<len(self.values) :
            self.values[key] = value
            """if we wanna make our list wide, we have to use "extend" like we used below, 
            it helps us to put our value in key if it bigger then len of list
            simply we add 0 until we reach key that we wanna put our value"""    
        elif key > len(self.values):
            self.values.extend([0] * (key - len(self.values)))
            self.values[key - 1] = value
        else:       
            raise IndexError("index out of range")    



    def __delitem__(self, key):
        if 0<key<len(self.values):
            del self.values[key]
        else:
            raise IndexError("index out of range")    


vect1 = Figures(11,23,21,11,23,445,45)
print(vect1[5])
vect1[2] = 5
print(vect1.values)
del vect1[2]
print(vect1.values)

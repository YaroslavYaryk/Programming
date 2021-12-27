class Vector(object):

    def __init__(self, *args):
        self.__x = args[0]
        self.__y = args[1]
        self.__z = args[2]
        self.__storage = list(args)

    def __repr__(self):
        return f"Vector ({self._x},{self._y},{self._z})"


    @property
    def get_x(self):
        return self.__x        

    @property
    def get_y(self):
        return self.__y

    @property
    def get_z(self):
        return self.__z        

    def __len__(self):
        return len(self.__storage) 

    def __getitem__(self, index):

        try :
            return self.__storage[index]
        except KeyError:
            return 0          


a = Vector(1,2,3)
print(len(a))
print(a[1:3])
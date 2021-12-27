class MyHashTable:
    size = 20
    
    def __init__(self):
        self._data = [None for _ in range(self.size)]
 
    def __getitem__(self, key):
        h = self.__get_hash(key)
        return self._data[h]
 
    def __setitem__(self, key, value):
        h = self.__get_hash(key)
        if self._data[h] is None:
            self._data[h] = value
        elif self._data[h] is not None and self._data[h+1] is None:
            self._data[h+1] = value
        else:
            self._data[h+2] = value            
 
    def __get_hash(self, name):
        return len(name) % self.size
 
m = {'Водоросли': 280,
     'Картофель': 260,
     'Лук-порей': 59,
     'Манго': 291,
     'Орехи грецкие': 266,
     'Салями': 225,
     'Специи': 283,
     'Сыр сливочный': 152,
     'Творог': 215,
     'Тофу': 142,
     'Хек': 248,
     'Чай черный': 118,
     'Чернила каракатицы': 95,
     'Шампиньоны': 101,
     'Финик': 104}
 
table = MyHashTable()
for k, v in m.items():
    table[k] = v
# print(table['Манго'])
print(table._data)
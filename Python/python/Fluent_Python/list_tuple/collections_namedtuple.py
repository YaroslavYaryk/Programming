from collections import namedtuple

Country = namedtuple('Country',"name population year capital")

Kyiv = Country("Ukraine",  "3500", "2021", "Kyiv" )
print(Kyiv)
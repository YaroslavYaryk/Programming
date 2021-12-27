
class Tiles(object):

	def __init__(self, brand, size_h, size_w, price):
		self.brand = brand
		self.size_h = size_h
		self.size_w = size_w
		self.price = price


	def getData(self):
		return f"Tiles({self.brand}, {self.size_h}, {self.size_w}, {self.price})"



a = Tiles("Leventom", 120, 70, 999)
b = Tiles("Lovy", 90, 30, 150)			
c = Tiles("Dirol", 240, 150, 1549)			
d = Tiles("Tommy", 50, 20, 99)			
e = Tiles("Chisy", 60, 40, 120)			

store = [a,b,c,d,e]
for elem in store:
	print(elem.getData())
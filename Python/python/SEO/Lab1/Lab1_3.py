import numpy as np

class Lister(object):

	def __init__(self, rows, cols):
		self.__rows = rows
		self.__cols = cols
		self.__array = [[]]


	def fill_array(self):
		self.__array = \
			np.random.randint(1,10, size = self.__rows*self.__cols) \
				.reshape(self.__rows,self.__cols)

	def swap_array(self):
		self.__array = self.__array.T

	def get_array(self):
		for i in self.__array:
			for j in i:
				print(j, end=" ")
			print()				


a = Lister(3,4)
a.get_array()
a.fill_array()
a.get_array()
print()
a.swap_array()
a.get_array()
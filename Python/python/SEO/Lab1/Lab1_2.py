
class Children(object):

	def __init__(self):

		self.__first_name = ""
		self.__last_name = ""
		self.__age = 0

	def get_data(self):
		return f"{self.__first_name} {self.__last_name} - {self.__age} years old"

	def set_data(self):
		name = input("enter name: ")
		surname = input("enter surname: ")
		age = int(input("enter age: "))
		if not (isinstance(name, str) and isinstance(surname, str) and
				isinstance(age, (int, float))):
			raise TypeError("Wrong type of data")
		self.__first_name = name
		self.__last_name = surname
		self.__age = age

a = Children()
b = Children()
c = Children()

store = [a,b,c]
for elem in store:
	elem.set_data()
	print(elem.get_data(), end="\n\n")
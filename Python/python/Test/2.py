from math import factorial


def find_sum(figure:int):
	fact = factorial(figure)
	return sum(int(i) for i in str(fact)), fact


print(find_sum(100))	
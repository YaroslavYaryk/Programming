

def is_central(string:str):
	lenth = len(string)
	if lenth %2==0:
		return False
	for i in range(lenth):
		if string[i] != " ":
			if lenth // 2 == i:
				return True
			return False	

print(is_central(" 2   "))

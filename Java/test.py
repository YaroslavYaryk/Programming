

def format_phone(numbers:str):

	return f"'({numbers[:3]}) {numbers[3:6]} {numbers[6:]}'"


print(format_phone('0000000000'))
print(format_phone('8005553535'))
print(format_phone('1234567890'))

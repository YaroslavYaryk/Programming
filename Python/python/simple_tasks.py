def get_perfect_time(seconds:int):

	second = seconds % 60
	seconds //= 60
	minutes = seconds % 60
	seconds //= 60
	hours = seconds % 24
	seconds //= 24
	days = seconds  

	print(f'{days}:{hours}:{minutes}:{second}')

# get_perfect_time(1234565)

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

# convert(1234565)

a = [1,2,3,4,5,5,6,7,6,5,1,9]

# print(a[0], a[-1])

def get_file_type(filename):
	if len(filename.split(".")) < 2:
		raise ValueError("Filename doesn't have dot")

	file_name = filename.split(".")[0]
	if not file_name:
		raise ValueError("empty name")
	file_type = filename.split(".")[-1]

	return(file_type)	

# print(get_file_type('abc.py'))
# print(get_file_type('abc'))  # raises ValueError
# print(get_file_type('.abc'))   # raises ValueError
# print(get_file_type('.abc.def.'))   # raises ValueError

def get_value(n:int):
	return n + int(str(n)*2) + int(str(n)*3)

# print(get_value(5))	

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
]

for elem in numbers:
	if elem == 237:
		break
	print(elem, end = " ") if elem % 2	==0 else print(end = "") 
d = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
arr = []
for elem in d.values():
    arr.append(elem)
arr = sorted(arr,reverse=True)
print(arr[0:3])  

print(int('ABC', 16))

def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n, 0)):
      print(row)
      row = [left + right for left, right in zip(row + y, y + row)]
   

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)

def someth(*args):
    a = []
    b = tuple()
    for i in args:
        a.append(i)
        b += tuple(i)
    print(a,b ,sep= "\n")    

someth("a b c s d f")    


def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(5245))
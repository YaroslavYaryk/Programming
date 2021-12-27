import itertools
import operator

a = itertools.count(1,5) #is an generator but the main problem of it is this one will never stop
#so if we try to convert it to list it'll be so disgussting
(next(a)) # this call is more then good

b = itertools.takewhile(lambda x: x<50, itertools.count(1,5))
#this one is the way better 'cause there is the end if iteration so we can sop it 
# just by initializing a lambda function 
(list(b))

v = itertools.compress( range(10),range(5))
#give  the firs element when the first element's element and second 
#are si,ilar by truelly
(list(v))

def hello(word):
    return word.lower() in "aoeiu"
(list(filter(hello, "wOrd")))

a = [5,4,2,8,7,6,3,0,9,1]
(list(itertools.accumulate(a))) # if there is no second operands 
# this function calculate num the value of it is sum the privious one and itself
 
(list(itertools.accumulate(a, min)))
#if there is second argument (min) it return generatir of elements 
# so if previous  elem is lowwer than current return previous one, else this one, step by step
 
(list(itertools.accumulate(a, max))) 
#if there is second argument (max) it return generatir of elements 
# so if previous  elem is bigger than current return previous one, else this one,q step by step
 
(list(itertools.accumulate(a, operator.mul))) 
# the next one is multiplaction of previous and itself

(list(itertools.product(range(3), range(3))))
#make tuples between first element of first operand and first elem of seconf operand ...........

a = [str(i) for i in range(1,11) ] + list("JOKA")
b = ("spades hearts diamonds clubs").split()
(list(itertools.product(a, b)))

(list(itertools.repeat(5,5))) #repeat "5" 5 times

(list(map(operator.mul, range(1,11), itertools.repeat(5))))
#multiply all element from 1 to 10

(list(itertools.combinations("abc", 2))) # buld all combination with first operand
# 2 elements in pair we can change this character
(list(itertools.combinations_with_replacement("53", 2)))
#the same as previous one but allow replacement

a = "LLLAASJDS"
for char, group in itertools.groupby(a): #create groups by some cperation 
    (f"{char} -> {list(group)}") 
    
a = ["hello", "world", "and", "everybody"]
for lenth, group in itertools.groupby(a, len): 
    print(f"{lenth} -> {list(group)}")     
#create groups by lenth of words    
from collections import Counter

string1 = [1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,8,7,6,5,4]
string2 = [1,21,13,14,15,14,13,12,11,12,13,14,5,6,7,8,8,7,6,5,4]

count = Counter(string1)  ##create a dictionary whete it count all values
count.most_common(3) ##show 3 the most common values in string
(count.elements())  ##make an iterator so we can loop it over
"""
for i in count.elements():
    print(i, end=" ") 

>>> 1 1 2 2 2 3 3 3 4 4 4 4 5 5 5 6 6 7 7 8 8  and sort it as well
"""
count1 = Counter(string1)
count2 = Counter(string2)

(count1 + count2) ## just add all the same position values to each other
## Counter({4: 8, 2: 6, 3: 6, 5: 6, 1: 4, 6: 4, 7: 4, 8: 4})
print(count1 - count2)##we can use different ass well
##Counter({2: 3, 3: 3, 4: 3, 1: 1, 5: 1})
count.clear() ##delete all value from counter
count1 & count2 ##show the minimum of two operands
count1 | count2 ##show the maximum of two operands

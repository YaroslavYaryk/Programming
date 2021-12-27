from collections import deque

a = deque(maxlen = 10) #default len is 10
for i in range(10):
    a.insert(i,i)

a.extend([22,11,33]) # we add 3 elements to the end so our firsl 3 element juse disapier
a.extendleft([123]) #the same way but here we add element to the left boundary
a.pop()
a.pop()
a.pop()
a.popleft()
a.popleft()
a.popleft()

print(a)

a.append(5)
a.appendleft(11)
print(a)

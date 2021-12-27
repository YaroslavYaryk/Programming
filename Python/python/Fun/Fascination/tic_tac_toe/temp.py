import numpy as  np

a = np.arange(1,10).reshape(3,3)
print(sum(sum(a)))
print()
print((a[0,0] +  a[1,1] +  a[2,2]))
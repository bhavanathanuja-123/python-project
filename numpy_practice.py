# list=[1,2,3,4]
# new=[]
# for i in list:
#     new.append(i**2)
# print(new)

# import numpy as np
# new=np.array([1,2,3,4])
# res=new**2
# print(res)

# import numpy as np
# new=np.array([56,98,70,79])
# s=new.nbytes
# print(s)

# import sys
# list=[56,98,70,79]
# g=sys.getsizeof(list)
# print(g)

# import numpy as np
# new=np.array([56,98,70,79,"abc","XYZ",(123)])
# print(new)
# s=new.nbytes
# print(s)

# import numpy as np
# n=np.arange(0,10)
# print(n)

# import numpy as np
# n=np.zeros(4)
# print(n)

# import numpy as np
# n=np.ones(4)
# print(n)

# import numpy as np
# m=np.full((2,3),9)
# print(m)






# import numpy as np
# n=np.arange(10,100+1,10)
# print(n)
# print(n.dtype)

# import numpy as np
# n=np.arange(1,51,5)
# m=np.linspace(0,100,15)
# print(n)
# print(m)

# import numpy as np
# a=np.arange(1,21)
# print("Shape:",a.shape)
# print("Dimension:",a.ndim)
# print("Data type:",a.dtype)
# print("Item size:",a.itemsize)
# print("Total memory:",a.nbytes)

# import numpy as np
# a=np.arange(1,25)
# print(a.reshape(2,12))
# print(a.reshape(4,6))
# print(a.reshape(2,3,4))

# import numpy as np
# a=np.array(10)
# print(a.ndim)
# print(a.shape)
# b=np.array([10,20,30,40,50])
# print(b.ndim)
# print(b.shape)
# c=np.array([[1,2,3],[4,5,6]])
# print(c.ndim)
# print(c.shape)

# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80,90,100])
# print(a[0])
# print(a[-1])
# print(a[2])
# print(a[-2])
# print(a[6])

# import numpy as np
# a=np.array([10,20,30,40,50,60,70,80,90,100])
# print(a[:5])
# print(a[-4:])
# print(a[2:8:1])
# print(a[0::2])
# print(a[::-1])

# import numpy as np
# a=np.arange(1,51)
# print("Even:",a[a%2==0])
# print("odd:",a[a%2!=0])
# print("multiples of 5:",a[a%5==0])
# print("numbers greater than:",a[a>30])

# import numpy as np
# a = np.array([5,10,15,20,25,30,35,40,45,50])
# print(a[1:5])
# print(a[[0,4,8]])

# import numpy as np
# a = np.array([    [10,20,30,40],    [50,60,70,80],    [90,100,110,120],    [130,140,150,160]])
# print(a[1,1])
# print(a[2,3])
# print(a[0])
# print(a[3])
# print(a[:,1])

import numpy as np
a = np.array([    [10,20,30,40],    [50,60,70,80],    [90,100,110,120],    [130,140,150,160]])
print(a[0:2])
print(a[:,-2:])
print(a[:3,:2])
print(a[1:3,1:3])
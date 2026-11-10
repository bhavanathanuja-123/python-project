# def single_number(a):
#     for i in a:
#         if a.count(i)==1:
#             print(i)
# a=[2,1,3,2,3]
# single_number(a)

# def palindrome(n):
#     temp=n
#     rev=0
#     while temp>0:
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10
#     return n==rev
# def next_palindrome(n):
#     n=n+1

#     while True:
#         if palindrome(n):
#             return n
#         n=n+1
# n=121
# print("Next Palindrome:",next_palindrome(n))

# def sort_colors(a):
#     a.sort()
#     return a
# a=[2,0,2,1,1,0]
# print(sort_colors(a))


import numpy as np
# n=np.random.rand(4,4)
# print(n)
# n=np.random.rand(3,3)
# print(n[n>0.5])
# n=np.random.randn(1,20)
# print(n)
# positive=n[n>0]
# negative=n[n<0]
# print(len(positive))
# print(len(negative))
# n[n>0]=0
# print("After replacing negative:")
# print(n)
# n=np.random.randint(1,100,25)
# print(n)
# print(np.max(n))
# print(np.min(n))
# print(np.mean(n))
# print(n[n%2==0])
# m=np.random.choice([35,45,55,65,75,85,95],size=4,replace=False)
# print(m)
# a=np.arange(1,21)
# print("Before shuffle:")
# print(a)
# np.random.shuffle(a)
# print("After shuffle:")
# print(a)
# n=np.arange(1,101,10)
# print("original array:")
# print(n)
# res=np.random.permutation(n)
# print(res)
# a=np.random.randint(0,101,20)
# print("student marks:")
# print(a)
# failed=a[a<40]
# passed=a[a>=40]
# distinction=a[a>=75]
# print("Failed students:",failed)
# print("Passed students:",passed)
# print("Distinction students:",distinction)
n=np.random.randint(20000,100001,15)
print("random salaries")
print(n)
print("salary greater than 50000:")
print(n[n>50000])
print("Salary between 30000 and 70000:")
print(n[(n>30000)& (n<70000)])
n[n<25000]=25000
print("Updated salaries:")
print(n)



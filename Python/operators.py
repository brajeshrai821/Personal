import sys
import os

#for num in range(10):
#    print(num)
#for num in range(0,10,2):
#    print(num)

for num in list(range(0,10,2)):
    print(num)

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

for item in zip(mylist1,mylist2):
    print(item)

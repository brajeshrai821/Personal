import os
import sys
import random
'''
a = 4 * (6+5)
print(a)

b = 3+ 1.5*4
print(type(b))

'''
'''
n = int(input("Enter Starting Number: "))
print(n)
m=(n ** 0.5)
print(m)
'''

'''
n = int(input("Enter Starting Number: "))
print(n)
m=(n ** 2)
print(m)
'''

'''
s= "hellow"
print(s[1])
#print(s[::-1])
print(s[-1])
'''
'''
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2]='goodbye'
print(list3)
'''
'''
list4 = [5,3,4,6,1]
print(sorted(list4))
print(list4.sort())
'''

d = {'simple_key':'hello'}
print(d.values())
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

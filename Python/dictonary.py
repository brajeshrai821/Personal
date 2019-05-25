import sys
import os
import random

'''
villans = {'mykey1': 'myvale1',
           'mykey2': 'myvale2',
           'mykey3': 'myvale3',
           'mykey4': 'myvale5'}


print(villans['mykey2'])
del villans['mykey1']

villans['mykey4'] = 'myvale4'
print(villans['mykey4'])

print(len(villans))

print(villans.get("mykey3"))
print(villans.keys())
print(villans.values())
'''

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print (my_dict['key3'])
print (my_dict['key3'][0])
print (my_dict['key3'][0].upper())

value= my_dict['key1']= my_dict['key1'] -123
print(value)

d= {'k1':123,
    'k2': [0,1,2],
    'k3':{'insidekey':100}
    }
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['insidekey'])

print(d.values())
print(d.keys())
print(d.items())

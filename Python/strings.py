import random
import sys
import os

'''

long_string = "I'll catch you in fall - The Floor"
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + "be there")
print("%c is my %s letter and my number %d is %.5f" %
      ('X', 'favourit', 1, .14))
print (long_string.capitalize())
print (long_string.find("Floor"))
print(long_string.isalpha())
print (long_string.isalnum())
print (len(long_string))
print (long_string.replace("Floor", "Replace"))
print (long_string.split())
print("\n")
print("\n")
print("\n")

quote_list = long_string.split(" ")
print(quote_list)
'''

'''
mystring = "Hello World"
print(mystring)

print(mystring[0])

mystring="tinker"
print(mystring[1:4])

name='sam'
last_letter=name[1:]
myname= 'p' + last_letter
print(myname)


x = 'Hello world'

print(x)

y =x.upper()
print(y)
z=y.lower()
print(x.split('o'))

print(z)
letter = 'z'
letter1 = letter * 10
print(letter1)
'''
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
print(result)

print(" The results was {}".format(result))
print(" The results was {r}".format(r=result))
print(" The results was {r:1.5f}".format(r=result))

name='raj'
print("Hello, his name is {}".format(name))
print(f'Hello his name is {name}')
age=30
print(f'{name} is {age} years old')

rule="rules"
print("Python {}".format(rule))

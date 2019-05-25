import random
import sys
import os

'''
random_num= random.randrange(0,100)

while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)


i = 0;

while(i <= 20):
  if(i%2 == 0):
      print(i)
  elif(i ==9):
      break
  else:
      i += 1
      continue

    i += 1
'''

x = 0

while x<5:
    print(f'the current value for x is {x}')
    x += 1

mystring = 'sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

for letter in mystring:
    if letter == 'a':
        break
    print(letter)

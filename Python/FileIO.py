import random
import sys
import os

'''
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

test_file1 = open("test.txt", "r+")
text_in_file = test_file1.read()
print(text_in_file)

#os.remove("test.txt")

n = int(input("Enter Starting Number: "))
print(n)
while n != 1:
    if (n % 2 == 0):
        n = n/2
        print(n)
    else:
        n = (3*n)+1
        print(n)


myfile= open('test.txt')
#print(myfile.read())
#myfile.seek(0)
#print(myfile.read())
#myfile.seek(0)
#contents = myfile.read()
#print(contents)
#myfile.seek(0)
print(myfile.readlines())
myfile.close()

with open('test.txt') as my_new_file:
    contents=my_new_file.read()
print(contents)

with open('myfile.txt', mode='r') as f:
    print(f.read())

with open('myfile.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('myfile.txt', mode='r') as f:
    print(f.read())
        
'''
with open('newfile.txt', mode='w') as f:
    f.write('This is a new file')

with open('newfile.txt', mode='r') as f:
    contents=(f.read())
    print(contents)
    type(contents)


raj.k@tcs.com

'''
for x in range(0,10):
    print(x, ' ', end="")
print("\n")

g_list = ['potatos', 'banana', 'milk'
          'icecream']

for y in g_list:
    print(y)

for x in [2,4,6,7,8,9]:
    print(x)
num_list=[[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])



for num in list1:
    print(num)

list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num%2 ==0:
        print(f'this below is an even {num}')
    else:
        print(f"Odd Number below is {num}")


mystring = "Hello World"
for letter in mystring:
    print(letter)
list2 = [(2,4),(6,8),(10,12)]

#for tup in list2:
#    print(tup)

for (t1,t2) in list2:
    print(t1)

list3 = [(2,4,5),(5,6,8),(7,3,1)]

for t3,t4,t5 in list3:
    print(t4)
'''
d = {'k1':1,'k2':2,'k3':3}

for items in d:
    print(items)

for items in d.items():
    print(items)

for keys,values in d.items():
    print(keys,values)

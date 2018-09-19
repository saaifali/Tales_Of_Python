#python code to illustrate use of filter, map and reduce with lambda.
from functools import reduce

#filter

li = [5,7,22,43,21,64,35,45,78,3,2,8,9]
print("Initial List : " + ', '.join(map(str,li)))
#get all odd numbers
fl = list(filter(lambda x: (x%2!=0), li))
print("Odd numbers using filter : "+ ', '.join(map(str, fl)))
#print(fl)

#new list with the values multiplied by 2.
fl2 = list(map(lambda x:x*2, li))
print("2x numbers using map : "+ ', '.join(map(str, fl2)))

#add all elements using reduce
fl3 = reduce((lambda x,y: x+y), li)
print("sum using reduce = "+str(fl3))
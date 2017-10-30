import math


def higher_square(n):
    x = math.sqrt(n)
    floor_integer = int(x)
    ceil_integer = floor_integer + 1
    return ceil_integer


n = input("Enter the number of key presses :")
c = 'a'
z = higher_square(n)
c = z*c
n=n-z
print z
print c + " : len = "+str(len(c))+" key presses left= "+str(n)
while(n>=3):
    n=n-3
    c=2*c
    print c + " : len = " + str(len(c)) + " key presses left= " + str(n)

temp = c


print c + " : len = " + str(len(c)) + " key presses left= " + str(n)

while(n>0):
    c = c + temp
    n=n-1
    print c + " : len = " + str(len(c)) + " key presses left= " + str(n)

print c
print len(c)

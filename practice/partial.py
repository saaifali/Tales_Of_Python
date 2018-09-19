from functools import partial


def add(a, b, c, d):
    return (a+b+c+d)


add60 = partial(add,10,20,30)

sum = add60(10)

print(sum)
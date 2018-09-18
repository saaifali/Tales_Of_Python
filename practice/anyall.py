# Here all the iterables are True so all
# will return True and the same will be printed
print(all([True, True, True, True]))

# Here the method will short-circuit at the
# first item (False) and will return False.
print(all([False, True, True, False]))

# This statement will return False, as no
# True is found in the iterables
print(all([False, False, False]))

print(any([True,False,False]))

a = any([True, True])

print(a)
class X(object):
    def __init__(self, a):
        self.num = a

    def doubleup(self):
        self.num *= 2


class Y(X):
    def __init__(self, a):
        super(Y, self).__init__(a)

    def tripleup(self):
        self.num *= 3


obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)




# Base or Super class
class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    def __init__(self, name, eid):
        ''' In Python 3.0+, "super().__init__(name)"
            also works'''
        super(Employee, self).__init__(name)
        self.empID = eid

    def isEmployee(self):
        return True

    def getID(self):
        return self.empID

    # Driver code


emp = Employee("Geek1", "E101")
print(emp.getName(), emp.isEmployee(), emp.getID())
from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def fromBirthYear(cls,name,year):
        age = date.today().year - year
        return cls(name, age)


    @staticmethod
    def isAdult(age):
        if age>=18:
            return True
        return False



p1 = Person("Saif",23)
p2 = Person.fromBirthYear("Goku", 1999)
print(p1.age)
print(p2.age)

print(Person.isAdult(25))
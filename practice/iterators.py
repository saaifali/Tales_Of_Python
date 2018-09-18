class Siterator:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = -1
        return self

    def __next__(self):
        val = self.x
        if val >= self.limit:
            raise StopIteration
        self.x = val + 1
        return self.x


obj = Siterator(15)

for i in obj:
    print(i)


ob2 = Siterator(20)
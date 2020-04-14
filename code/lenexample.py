class Foo:

    def __init__(self, length=5):
        self.length = 5

    def __len__(self):
        return self.length


f = Foo()
length = len(f)
print(f"Length of the f object is {length}")
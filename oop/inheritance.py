class Dog():
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name+" is sitting")


d = Dog("Gulisto")
d.sit()
print("The dog's name is :", d.name)


class CloneDog(Dog):

    def __init__(self, name):
        super().__init__(name)  # copy constructor

    def search(self):
        print("The dog", self.name, " is searching")


cd = CloneDog("Roomie")

cd.sit()

cd.search()

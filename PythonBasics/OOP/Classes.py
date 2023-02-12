class MyClass():

    # obje türetilirken alınması zorunlu olmayan parametre
    weight = 70 

    #bir sınıftan obje türetildiğinde bu fonksiyon çağırılır. hazır fonksiyon
    def __init__(self, name, age, active):
        #obje türetilirken alınması zorunlu parametreler
        print("init called")
        self.name = name
        self.age = age
        self.active = active

    #method oluştururken parametreye self eklenmezse uygulama çöker
    def setWeight(self, weight):
        self.weight = weight

#INHERITANCE sınıfımdan miras aldı
class MyClass2(MyClass):
    def __init__(self, name, age, active):
        super().__init__(name, age, active)
    #ana sınıftaki methodun üzerine yazılabilir override
    def setWeight(self, weight):
        self.weight = weight * 2

myObject = MyClass2("myName", 30, True)

print(myObject.name)
print(myObject.weight)
myObject.setWeight(80)
print(myObject.weight)
print()

#POLYMORPHISM
print("POLYMORPHISM:")
class Apple():
    def info(self):
        print("This is Apple object")
class Banana():
    def info(self):
        print("This is Banana object")
class Orange():
    def info(self):
        print("This is Orange object")

fruitList = [Apple(), Banana(), Orange()]
# tamamen ayrı sınıflar olmasına rağmen method isimlerinin aynı olması yeterli oldu
for fruit in fruitList:
    fruit.info()
print()
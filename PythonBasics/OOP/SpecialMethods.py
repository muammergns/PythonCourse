class MyClass():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    # bu fonksiyon print çağırıldığında çalışır
    def __str__(self) -> str:
        return self.name
    
    # bu fonksiyon len çağırıldığında çalışır
    def __len__(self) -> int:
        return self.age

myObject = MyClass("myName", 30)
print(myObject)
print(len(myObject))

#bunlar sadece örnek. internette çok fazla special method bulunuyor açıklamaları ile birlikte

while True:
    try:
        # burası ilk çalışmada denenir
        newInt = int(input("Enter number:"))
    except:
        # hata varsa buraya geçer
        print("Except")
    else:
        # hata yoksa buraya geçer
        print("Else")
    finally:
        # hata olsada olmasada çalışır
        print("Finally")
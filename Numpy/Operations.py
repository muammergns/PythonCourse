import numpy as np

myList = np.random.randint(1,100,20)
print(myList)
#bool list döndürür
print(myList > 24)
#listedeki 24ten büyük sayıları yeni bir liste olarak döndürür
print(myList[myList > 24])
print()

myArray = np.arange(0,24)
print(myArray)
#listedeki tüm elemanları 2 ile çarpabiliriz
print(myArray * 2)
#karekök alma sinüsünü alma gibi belli matematiksel işlemleri kolayca yapabilir
print(np.sqrt(myArray))
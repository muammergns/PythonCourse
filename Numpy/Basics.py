import numpy as np

#numpy array
myList = [20, 30, 40]
print(type(myList))

myArray = np.array(myList)
print(type(myArray))

matrixList = [[1,2,3],[2,3,4],[3,4,5]]
matrixArray = np.array(matrixList)
print(matrixArray)

#ARANGE
print("ARANGE:")
# 0dan 10 a kadar array oluştur
print(np.arange(0,10))
# 0dan 20ye kadar 2 atlayarak değer oluştur
print(np.arange(0,20,2))
print()

#ZEROS and ONES
print("ZEROS and ONES")
# 5 elemanlı tek boyutlu dizi oluştur ve tüm elemanları 0 olsun
print(np.zeros(5))
# 5x5 elemanlı 2 boyutlu dizi oluştur ve tüm elemanlar 1 olsun
print(np.ones((5,5)))
print()

#LINSPACE
print("LINSPACE:")
# 0dan 10a kadar eşit aralıklı 20 adet değer oluştur
print(np.linspace(0,10,20))
print()

#EYE
print("EYE:")
# 5x5 dizi oluştur satır numarasına karşılık gelen kolonu 1 yap diğerleri 0 olsun
print(np.eye(5))
print()

#RANDOM
print("RANDOM")
# 0-1 arasında 6 adet random list oluştur
print(np.random.randn(6))
print()
# 0-1 arasında 6x6 şeklinde 2 boyutlu random bir dizi oluştur
print(np.random.randn(6,6))
print()
# 0-2 arasında (2 dahil değil) bir sayı türet
print(np.random.randint(0,2))
print()
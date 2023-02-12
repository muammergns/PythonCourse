import numpy as np

myList = np.arange(0,15)
print(myList)
#listenin 3ten 5e kadar elemanları getir 5. hariç
print(myList[3:5])
#listenin 3ten 5e kadar elemanları -5 yap 5. hariç
myList[3:5] = -5
print(myList)

#0dan 24e kadar yeni bir liste oluştur
myList2 = np.arange(0,24)
#4ten 9a kadar olan elemanları yeni bir listeye çek
slicingList = myList2[4:9]
print(slicingList)
#yeni listenin tüm elemanlarını 700 yap
slicingList[:] = 700
print(slicingList)
#buradaki sorun şu ilk oluşturulan listenin elemanlarıda 700 oldu
print(myList2)

#böyle bir sorun olmaması için:
#0dan 24e kadar yeni bir liste oluştur
myList3 = np.arange(0,24)
#ayrı bir liste oluştur
myList4 = myList2.copy()
# artık myList4 üzerinde istenen işlem yapılabilir
print()

#MATRIX INDEX
print("MATRIX INDEX")
myMatrix = [[10,20,30],[20,30,40],[40,50,60]]
matrixArray = np.array(myMatrix)
print(matrixArray)
#Listle aynı sistem
print(matrixArray[0,0])
print(matrixArray[0:,0])

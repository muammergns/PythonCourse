#RANGE
print("RANGE:")
print(list(range(25)))#0 dan 24e kadar liste oluşturur
print(list(range(5, 21, 4)))#5ten başla 21e kadar git ve 4 ekleyerek ilerle
print()

#ENUMERATE
print("ENUMERATE:")
print(dict(enumerate(list(range(5,21,4)))))#tuple ile elemanları dict olarak eşleştiriyor
print()

#RANDOM
print("RANDOM:")
from random import randint
randList = []
for x in range(20):
    randList.append(randint(0,100))#rastgele sayılar üretiliyor
print(randList)

from random import shuffle
randList = list(range(20))
shuffle(randList)#listenin elemanları karıştırır
print(randList)
print()

#ZIP
print("ZIP:")
list1 = list(range(5))
shuffle(list1)
list2 = list(range(5))
shuffle(list2)
list3 = list(range(5))
shuffle(list3)
zipList = zip(list1, list2, list3)#listeleri birleştiriyor
print(list(zipList))
print()

#HELP
print("HELP:")
print(help(randList.clear))#bu şekilde bir fonksiyonun ne işe yaradığı alınabilir
print()
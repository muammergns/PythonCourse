
# LIST
print("LIST:")
fisrtString = "Hello World!"
print(fisrtString)
print(fisrtString[0])
#fisrtString[0] = "B" #hata verecektir immutability
#print(fisrtString[0])

numList = [10, 20, 30]
print(numList)
numList[0] = 40
print(numList) #mutable yani değiştirilebilir
numList.append(50) #listeye yeni eleman ekleme
print(numList)
#numList.clear() #listeyi temizler
numList.pop() #son elemanı listeden çıkarır
print(numList)
numList.remove(40) #bu elemanı listeden çıkar
print(numList)
print(numList.count(20)) #listede bu elemandan kaç tane var
numList.reverse() # listeyi ters çevirir
print(numList)
numList.append(fisrtString) #illa hepsi aynı data tipi olmak zorunda değil
print(numList)
numList.append([1,2,3]) # liste içinde liste bile olabiliyor
print(numList)
print()

# DICTIONARY
print("DICTIONARY:")
numDict = {"key" : "value", 1:"val1",2:"val2",3:"val3"}
print(numDict)
numDict[1] = "newVal"
print(numDict)
print(numDict.keys()) #keyleri liste halinde verir
print(numDict.values()) #değerleri liste halinde verir
print()

#SET
print("SET:")
numSet = {10, 20, 30, 30} # sözlük gibi oluşturulur ancak aynı elemandan 2 adet eklenemez
print(numSet)
print()

#TUPLE
print("TUPLE:")
numTuple = (1,2,"a",4.5) #değiştirilemez liste
print(numTuple)
print()
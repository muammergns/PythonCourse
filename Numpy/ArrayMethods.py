import numpy as np

#RESHAPE
print("RESHAPE:")
#0-100 arası 100 hariç 20 adet rastgele sayı üret
myList = np.random.randint(0,100,20)
print(myList)
#üretilen sayı listesini 4x5 matrix haline getir
print(myList.reshape(4,5))
print()

#MAX MIN
print("MAX MIN:")
print(myList.argmax())
print(myList.max())
print(myList.argmin())
print(myList.min())
print()


import numpy as np
import matplotlib.pyplot as mp

# bana bir liste türet
# standart sapması 500 olsun
# 1000 adet değer üret
myList = np.random.normal(4000, 500, 1000)
print(np.mean(myList))

mp.hist(myList,50)
mp.show()

# numpy bu verileri oluşturmada bize yardımcı oldu
# matplot bu verileri görselleştirmede bize yardımcı oldu
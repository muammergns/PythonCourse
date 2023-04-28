import numpy as np
import pandas as pd

#pandas veri biliminin exceli
#excel ile çalışıyormuş hissi verir
#numpydan türetilmiş diyebiliriz

#SERIES
#serileri listlerden numpy arrayden sözlüklerden kolayca oluşturabiliriz
print("SERIES:")
myDict = {"num1":50,"num2":40,"num3":30}
print(pd.Series(myDict))
print()

myListVals = [50,40,30]
myListKeys = ["num1","num2","num3"]
print(pd.Series(myListVals))
print()

print(pd.Series(data=myListVals,index=myListKeys))
print()

myArrays = np.array([50,40,30])
print(pd.Series(myArrays))

print()

#SERIES FEATURES
print("SERIES FEATURES")
mySeries1 = pd.Series([10,5,1],["num1","num2", "num3"])
print(mySeries1)
mySeries2 = pd.Series([20,10,8],["num1","num2", "num3"])
print(mySeries2)
print()
myResultSeries = mySeries1 + mySeries2
print(myResultSeries)
print()

# kursta burası çökmez dendi ama bende çöküyor
# muhtemelen vsc ile denediğim için pycharm ile denemek lazım
#mySeries3 = pd.Series([20,30,40,50],"a","b","c","d")
#mySeries4 = pd.Series([10,5,3,1], "a","c","f","g")
#print(mySeries3 + mySeries4)

print()
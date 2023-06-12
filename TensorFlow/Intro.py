import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

dataFrame = pd.read_excel("bisiklet_fiyatlari.xlsx")
print(dataFrame.head())
#sbn.pairplot(dataFrame)
#plt.show()
#NOTE - bu kısımda atıl hocanın hazırladığı test dosyası çekildi ve gösterildi

from sklearn.model_selection import train_test_split
# y = wx + b
# y -> label
y = dataFrame["Fiyat"].values
# x -> feature (özellik)
x = dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33,random_state=15)
#NOTE - çekilen tablo test ve eğitim olarak rastgele dağıtıldı

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
#NOTE - tablodaki özellikler adında 2 kolon 0-1 arasında normalize edildi

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
#NOTE - burada importla ilgili sorunlar yaşandı
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# şeklinde import etmem gerekiyordu ancak bende çalışmadı
# bende bu şekilde çalığtığını farkettim ve ellemedin

model = Sequential()
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(1))
model.compile(optimizer="rmsprop",loss="mse")
#NOTE - model oluşturuldu, öğrenme açısından kursta verilen değerlerin dışına çıkmadım
# bu yüzden Jupyter eklentisini kurdum, ilerleyen zamanlarda kendi testlerimi rahatlıkla yapacağım


model.fit(x_train,y_train,epochs=250,verbose=0)
#NOTE - tam burada eğitim işlemi gerçekleşiyor
# Jupyter avantajı kodları satır satır çalıştırabilmek böylece örneğin train yaptıktan sonra verilerle istediğim gibi testler yapabilirim

loss=model.history.history["loss"]
sbn.lineplot(x=range(len(loss)),y=loss)
plt.show()
#NOTE - eğitimin sonuçları tablo olarak gösterildi

trainLoss = model.evaluate(x_train,y_train,verbose=0)
testLoss = model.evaluate(x_test,y_test,verbose=0)
print(trainLoss)
print(testLoss)
#NOTE - burada model değerlendiriliyor train ve test değerleri karşılaştırıyor. bir çeşit ön değerlendirme
# loss değerleri birbirine ne kadar yakınsa ve düşükse modelimin o kadar iyi durumdadır

testTahminleri = model.predict(x_test)
#NOTE - test değerlerimizle tahminde bulunmasını istiyoruz
testTahminleri = pd.Series(testTahminleri.reshape(330,))
tahminDf = pd.DataFrame(y_test,columns=["Real Y"])
tahminDf = pd.concat([tahminDf,testTahminleri],axis=1)
tahminDf.columns = ["Real Y","Tahmin Y"]
sbn.scatterplot(x="Real Y", y="Tahmin Y",data=tahminDf)
plt.show()
#NOTE - son olarak tahmin edilen değerler grafikleştiriliyor
# buradaki tüm kodlar Jupytere aktarıldı
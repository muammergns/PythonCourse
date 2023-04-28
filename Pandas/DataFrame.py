import pandas as pd
import numpy as np

data = np.random.randn(4,3)
print(data)
print()
dataFrame = pd.DataFrame(data)
print(dataFrame)
print()

newDataFrame = pd.DataFrame(data, index=["a","b","c","d"], columns=["x","y","z"])
print(newDataFrame)
print()
print(newDataFrame["x"])
print()
print(newDataFrame.loc["c"])
print()
print(newDataFrame.iloc[2])
# burada anlaşılması gereken durum kolonlara ve satırlara erişilebilirliğin kolaylığı
# ilerleyen bölümlerde excel ile çalışırken çok daha anlaşılır olacaktır
print()

# YENİ KOLON EKLEME
newDataFrame["n"] = newDataFrame["x"] + newDataFrame["y"] + newDataFrame["z"]
print(newDataFrame)
# yeni kolonu her satırın toplamı olarak kod içinde sonradan oluşturduk
print()

# KOLON SİLME
print(newDataFrame.drop("z", axis=1))
# axis=1 eklememizin sebebi default olarak axis değişkeninin 0 yani row ayarlı olması
# ancak biz kolon silmek istiyoruz, bu yüzden axis 1 yani kolon olarak ayarlamak gerekli
# sonradan kütüphanede güncelleme olabilir ve kodlamada hatalar çıkmaması adına bu tür parametlerelere dikkat edilmelidir
# ayrıca drop forksiyonu ana değişkeni bozmadan yeni bir tablo oluşturur istenirse ana tabloya eşitlenebilir
# ya da inplace=True parametresi ekleyerek eşitleme yapmadanda yapılabilir
# ancak ilerleyen bölümlerde listemi bozmamak adına eşitleme yapmıyorum. görünmesi yeterli
print()

# DİĞER INDEX ÖZELLİKLERİ
print(newDataFrame.loc["a","x"]) # önce satır sonra sütun yazılmalı, tek değer çekmek için
print()
print(newDataFrame > 0) # boolean tablo döndürür
print()
print(newDataFrame[newDataFrame > 0]) # 0'dan küçük olanları nan olarak gösterir
print()
print(newDataFrame[newDataFrame["x"] > 0]) # x kolonunda 0'dan küçük olanları satırdan çıkarıyor bu önemli
print()
newDataFrame.reset_index(inplace=True)
print(newDataFrame) # index adında yeni bir kolon oluşturur ve indexleri 0,1,2,3 şeklinde sıralar
print()
newIndexList = ["aa","bb","cc","dd"]
newDataFrame["nn"] = newIndexList
print(newDataFrame) # yeni index listesi kolon olarak eklendi
print()
newDataFrame.set_index("nn",inplace=True)
print(newDataFrame) # yeni index listesi index olarak atandı ayrıca eski index, index adındaki yeni kolona aktarıldı
print()

# MULTI INDEX
groupIndexes = ["group0","group0","group0","group1","group1","group1"]
inlineIndexes = ["g0.0","g0.1","g0.2","g1.0","g1.1","g1.2"]
allIndexes = pd.MultiIndex.from_tuples(list(zip(groupIndexes,inlineIndexes))) # burada 2 adet listeyi tupple liste dönüştürüp pandasa çeviriyoruz
print(allIndexes)
print()
myDataList = [[1,"a"],[2,"b"],[3,"c"],[4,"d"],[5,"e"],[6,"f"]] # data set oluşturuldu
myNumpyList = np.array(myDataList) # data setimiz numpy dizisi haline getirildi
myListDataFrame = pd.DataFrame(myNumpyList, index=allIndexes, columns=["number","letter"])
# artık son olarak data set ile indexler birleştirilip dataframe haline getirildi
print(myListDataFrame)
print()
print(myListDataFrame.loc["group0"]) # sihirli bölüm burası
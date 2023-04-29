import pandas as pd
import numpy as np

#EKSİK VERİ GELDİĞİNDE NE YAPACAĞIZ
data = {"room1":[20,30,np.nan],"room2":[23,np.nan,43],"room3":[25,35,45],"room4":[27,np.nan,np.nan]}
tempDataFrame = pd.DataFrame(data)
print(tempDataFrame)
#eksiklerle dolu bir veri seti oluşturuldu
#bunun aslında pek radikal bir çözümü yok
#çözüm bir içinde nan bulunan verileri listeden çıkarmak
#çözüm 2 içinde nan bulunan verileri kolondan çıkarmak
#çözüm 3 nan olanları verilerle doldurmak
#aslında burada önemli olan konu verilerin hassasiyeti
#eğer sistemimizi bozmayacaksa ortalama alıp boşları doldurmak bile çözüm olabilir
print()
print(tempDataFrame.dropna())
print()
print(tempDataFrame.dropna(axis=1))
print()
print(tempDataFrame.dropna(axis=1, thresh=2))
print()
print(tempDataFrame.fillna(50))
print()

#GROUPBY
groupByDict = {
    "group":["group0","group0","group1","group1","group2","group2"],
    "member":["member0","member1","member2","member3","member4","member5"],
    "number":[100,200,300,400,500,600]
}
groupByFrame = pd.DataFrame(groupByDict)
print(groupByFrame,"\n")
groupByObj = groupByFrame.groupby("group")
print(groupByObj.count(),"\n")# hangi grupta kaç tane veri varsa tablolaştırıyor
print(groupByObj.mean(numeric_only=True),"\n")# her grup için numeric olanların ortalamasını alıyor
print(groupByObj.min(),"\n")# her grup için en düşük sayı olanı gösteriyor
print(groupByObj.max(),"\n")# her grup için en yüksek sayı olanı gösteriyor
print(groupByObj.describe(),"\n")# her grubun istatistiklerini çıktı veriyor
import pandas as pd
import numpy as np

dict1 = {
    "name":["name0","name1","name2","name3","name4","name5"],
    "activity":["activity0","activity1","activity2","activity3","activity4","activity5"],
    "number":[100,200,300,400,500,600]
}
dict2 = {
    "name":["name6","name7","name8","name9","name10","name11"],
    "activity":["activity6","activity7","activity8","activity9","activity10","activity11"],
    "number":[700,800,900,1400,1500,1600]
}
dict3 = {
    "name":["name12","name13","name14","name15","name16","name17"],
    "activity":["activity12","activity13","activity14","activity15","activity16","activity17"],
    "number":[2100,2200,2300,2400,2500,2600]
}
frame1 = pd.DataFrame(dict1, index=[0,1,2,3,4,5])
frame2 = pd.DataFrame(dict2, index=[6,7,8,9,10,11])
frame3 = pd.DataFrame(dict3, index=[12,13,14,15,16,17])
print(frame1,"\n")
print(frame2,"\n")
print(frame3,"\n")

#CONCATENATION
#dataframeleri birleştirmek için kullanılabilir bir sistem kurulmuş
#ancak harikalar yaratıyormuş gibi gelmedi çünkü 
# kolon sayıları kolon isimleri uyumlu olacak 
# bunun yanında indexlere dikkat edilmesi gerekiyor 
# işlevselliği tartışılır yinede yapılabiliyor olması güzel
print(pd.concat([frame1,frame2,frame3]),"\n")


dict4 = {
    "name":["name0","name1","name2","name3","name4","name5"],
    "number":[100,200,300,400,500,600]
}
dict5 = {
    "name":["name0","name1","name2","name3","name4","name5"],
    "activity":["activity0","activity1","activity2","activity3","activity4","activity5"]
}
frame4 = pd.DataFrame(dict4)
frame5 = pd.DataFrame(dict5)
print(frame4,"\n")
print(frame5,"\n")

#MERGE
# birleştirme işleminde concat gibi belirli koşullar altında gerçekleşiyor 
# aslında aldığım eğitimde detay verilmemiş keşfetmek gerekiyor 
# fonksiyona parametreler eklenip daha karmaşık işlemler yapılabilir gibi geliyor 
# yani bu kadar basit olamaz
print(pd.merge(frame4,frame5, on="name"),"\n")


dict6 = {
    "name":["name0","name1","name2","name2","name4","name5"],
    "activity":["activity0","activity1","activity2","activity3","activity4","activity5"],
    "number":[100,200,300,400,500,600]
}
frame6 = pd.DataFrame(dict6)

# OTHER FUNCTIONS

print(frame6["name"].unique(),"\n")# verimizde 2 adet name2 var. sadece tek olanları getir demek
print(frame6["name"].nunique(),"\n")# kaç tane tek veri var
print(frame6["name"].value_counts(),"\n")# hangi veriden kaç tane var
def myFunc(num):
    return num * 0.66
print(frame6["number"].apply(myFunc),"\n")# frame bir fonksiyona bile uygulanabilir haaarika
print(frame6.isnull(),"\n") # boş ya da hatalı değer var mı şeklinde tüm tabloyu true false olarak listeler


dict7 = {
    "name":["name0","name0","name1","name1","name1","name1"],
    "activity":["activity0","activity1","activity2","activity3","activity4","activity4"],
    "number":[100,200,300,400,500,600]
}
frame7 = pd.DataFrame(dict7)
print( frame7.pivot_table(values="number", index=["name","activity"]),"\n")
# yapılan işlem gördüğüm kadarıyla şu 
# öncelikle 2 index oluşturup indexleri gruplandırdı
# grup ve index olacak kolonları biz belirttik
# aynı index olanların sayılarını ortalama aldı
print( frame7.pivot_table(values="number", index=["name","activity"], aggfunc=np.sum),"\n")
# bir parametre ekleyerek ortalama almak yerine toplamasını istedik
# daha öncede belirtmiştim, foksiyonları genelde sade halleri ile kullanıyoruz
# parametreleri kurcaladıkça çok daha gelişmiş özellikler bulacağıma eminim








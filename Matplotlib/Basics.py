import numpy as np
import matplotlib.pyplot as plt

list1 = [10,20,30,30,30,40,50,60,70,75]
list2 = [20,60,80,85,86,87,70,90,95,90]

numpyList1 = np.array(list1)
numpyList2 = np.array(list2)

plt.plot(numpyList1,numpyList2,"g") # "g" burada rengi ifade ediyor green
plt.xlabel("List1")
plt.ylabel("List2")
plt.title("Change graph of List 1 versus List 2")
plt.show()
# grafikler gayet güzel görselleştirilebiliyor

numList1 = np.linspace(0,10,20)
numList2 = numList1 ** 3
plt.subplot(1,2,1)# 1 satırlı 2 kolonlu grafiğin 1.si
plt.plot(numList1,numList2,"b*-") 
plt.subplot(1,2,2)# 1 satırlı 2 kolonlu grafiğin 2.si
plt.plot(numList2,numList1,"b--") 
# subplot(nrows, ncols, index, **kwargs)
# tek seferde birden fazla grafik çizilebilir karşılaştırılabilir olması için
# "b--" mavi kesik çizgi
# "b*-" mavi veri noktalarına * yerleştirir
plt.show()


figure = plt.figure()
# 2 örnek yaptık ve basitçe bir grafik gösterdik
# aslında bunun temel düzeyi figure olarak ifade ediliyor
# boş bir figure oluşturulduğunda bir çerçeve oluşuyor
# önce eksenler oluşturulmalıdır
figureAxes = figure.add_axes([0.12,0.1,0.85,0.8])
# eksenler oluşturulurken parametreler bir liste halinde veriliyor biraz karmaşık olmuş
# 0:sol tarafın başlangıç noktası
# 1:alt tarafın başlangıç noktası
# 2:sol genişlik
# 3:alt genişlik
figureAxes.plot(numList1,numList2,"g")
figureAxes.set_xlabel("X")
figureAxes.set_ylabel("Y")
figureAxes.set_title("Title")
plt.show()
# kursta bu görüntü ekrana tam otururken bende ekrana tam sığmadı
# nedenini bilmiyorum ancak gayet uygun şekilde çalışıyor
# nedeni çözüldü VSC içinde sabit genişlikli bir pencere oluşturduğu için ekrana tam sığmıyor
# genişlik küçültüldüğünde düzeliyor

figure2 = plt.figure()
axis1 = figure2.add_axes([0.1,0.1,0.8,0.8])
axis2 = figure2.add_axes([0.2,0.5,0.3,0.3])

axis1.plot(numList1,numList2,"g")
axis1.set_title("Axis1 Title")

axis2.plot(numList2,numList1,"b")
axis2.set_title("Axis2 Title")
plt.show()
# 2 grafik iç içe gösterim yapılabiliyor
# 2 grafiğin boyutları ayarlanabiliyor
# pozisyonları değiştirilebiliyor
# figure kullanmak çok daha gelişmiş grafikler oluşturmaya yarıyor

(figure3, axis3) = plt.subplots(nrows=1, ncols=2)
for ax in axis3:
    ax.plot(numList1,numList2,"g")
plt.tight_layout()# görüntüyü otomatik olarak düzeltiyor
plt.show()

numList = np.linspace(0,10,20)

figure = plt.figure(figsize=(8,8),dpi=80)
axis = figure.add_axes([0.1,0.1,0.85,0.85])
axis.plot(numList,numList ** 2,label="numlist ** 2")
axis.plot(numList,numList ** 3,label="numlist ** 3")
axis.legend(loc=6)# legend eksenin rengi ve etiketi ile ile birlikte bir kutu oluşturur
plt.show()
figure.savefig("figure.png",dpi=200) # bu komut grafiği png dosyası olarak kodun bulunduğu klasöre kaydeder
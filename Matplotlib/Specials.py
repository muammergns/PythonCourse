import numpy as np
import matplotlib.pyplot as plt

numList = np.linspace(0,10,20)

(figure, axis) = plt.subplots()
axis.plot(numList,numList+2,color="#3a95a8",alpha=0.3)# renk kodu ve saydamlık verilebilir
axis.plot(numList,numList+3,color="#c96f23")# renk kodu ile gösterilebilir
axis.plot(numList,numList+4,color="RED",linewidth=5)# çizgi kalınlığı değiştirilebilir
axis.plot(numList,numList+5,"g",linestyle="-.")# çizgi nokta stili
axis.plot(numList,numList+6,"g",linestyle=":")# nokta nokta stili
axis.plot(numList,numList+7,"g",linestyle="--")# çizgi çizgi stili
axis.plot(numList,numList+8,color="BLACK",marker="o",markerfacecolor="RED",markersize=10)
# her değer noktasına marker koyulabilir, bu markerın stili seçilebilir, markerın ortasına renk verilebilir, boyutu ayarlanabilir
plt.show()

# SCATTER
# tüm değerleri birleşmiş çizgi yerine nokta nokta gösterir
# gidişat yerine değerlerin önemli olduğu durumlarda gösterilebilir
plt.scatter(numList,numList**2)
plt.show()

# HISTOGRAM
# çubuk grafik
nplist = np.random.randint(0,100,50)
plt.hist(nplist)
plt.show()

# BOXPLOT
# değerlerin dağılım grafiği
plt.boxplot(nplist)
plt.show()

# matplotlib kursta tamamlandı ancak çok geniş bir kütüphane
# internetteki tutoriallara bakılabilir ve bunlar denenebilir
# diğer kütüphaneler gibi detaylara inmek için önce kullanmak gerekir
# kullandıkça lazım oldukça çok daha iyi öğrenilecektir
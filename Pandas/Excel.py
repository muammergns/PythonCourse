import pandas as pd
from os.path import dirname, join
current_dir = dirname(__file__)
dataFrame = pd.read_excel(current_dir + "\\test.xlsx")
print(dataFrame,"\n")
# pandas ile direkt olarak dosya okuma yapılabliyor
# çeşitli dosya formatlarını rahatlıkla okuyabiliyor
# operasyonlardaki işlemleri uygulayıp yeni bir excel dosyası oluşturmakta mümkün
nonNullDataFrame = dataFrame.dropna()
print(nonNullDataFrame,"\n")
# null değeri olmayan sadece 4 tane satırım var
# ve bu yeni tablomu excel olarak kaydetmek istiyorum
nonNullDataFrame.to_excel(current_dir + "\\newTest.xlsx")
# gayet güzel bir şekilde çıktısını aldı

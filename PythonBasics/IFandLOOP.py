#IF
print("IF")
if False :#tab boşluğu çok önemli
    print("Hello World!")
print("tab test")
x,y = 3,4

if x < y :
    print("y GT x")
elif x > y:
    print("y LT x")
else:
    print("y EQ x")
print()

#FOR
print("FOR")
numList = [1,2,3]
for num in numList: #listenin tamamını döngüye alır
    print(num)

for x in range(100):
    if x%20 == 0 and x !=0:
        if x == 20:# x 20 ise devam eden kodları çalıştırma ve başa dön
            continue
        print(x)

for x in range(10000):
    pass #bu loop çalışmaz
print()

#WHILE
print("WHILE")
num = 10
while num>0: #num 0dan büyük olduğu sürece döngüde kalır
    num=num-1
    if num == 5:#num 5e eşitse döngüyü kır
        break
print(num)
print()
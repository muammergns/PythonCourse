#FUNCTIONS
print("FUNCTIONS:")
def firstFunc():
    print("Hello World")

firstFunc()#fonksiyonu önce oluşturup daha sonra çağırmak lazım satır sıraları önemli

def func1(firstInput):
    print(firstInput)

func1("Hello World!")#fonksiyona input gönderirken data tipi önemli değil
func1(16384)

def func2(input = "Hello"):
    print(input)

func2()#input vermeye gerek kalmayabiliyor
func2("World")

def func3(num1, num2):
    print(num1+num2)

func3(15,25)

def func4(num1, num2):
    return num1 + num2

print(func4(150,200))
#fonksiyonlarda da tab boşluğu önemli
print()

#ARGS & KWARGS
print("ARGS & KWARGS:")
def myAddFunc(*args):#inputun başına * ekleyince sayısız giriş alınabiliyor
    print(args)#tuple geliyor
    num = 0
    for x in args:
        num = num + x
    return num

print(myAddFunc(1,2,3,4,5,6,7,8,9))
print(myAddFunc(10,20,30))

def mykwargs(**kwargs):
    return kwargs

print(mykwargs(a=10,b=20,c=30))#dict geliyor
print()
#sınıflar içinde kullanılan fonksiyonlara method deniyor ufak farklılıkları var
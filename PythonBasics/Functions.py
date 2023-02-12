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

#MAP
print("MAP:")
def mapFunc(number):
    return number / 2
print(list(map(mapFunc,list(range(20)))))
#map fonksiyonu for loopla uzun uzun yapılacak bir işlemi tek satırda kolayca yapmamızı sağlıyor
print()

#FILTER
print("FILTER:")
def filterFunc(text):
    return "s" in text
#içinde "s" olan stringleri liste halinde aldık
loremText = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(list(filter(filterFunc,loremText.split(" "))))
print()

#LAMBDA
print("LAMBDA:")
lambdaFunc = lambda num : num * 2
#basit fonksiyonlar bu şekilde kısaca yazılabilir
print(lambdaFunc(10))
print()

#LOCAL, ENCLOSING, GLOBAL, BUILD-IN
print("LOCAL, ENCLOSING, GLOBAL, BUILD-IN")
number = 1#global
def func5():
    number = 2#enclosing
    def func6():
        number = 3#local
        print(number)
    func6()

func5()
#aynı isimde değişken oluşturulduğunda sırasıyla LOCAL, ENCLOSING, GLOBAL, BUILD-IN kontrol edilir ve o değişken çağırılır
print()
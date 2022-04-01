
def odejmowanie(x, y):
    print (x-y)

def dodawanie(x, y):
       print (x+y)

def powitanie():
    print ('HEJ')
powitanie()

operacja,x,y=input().split()
print(operacja)
if operacja=="dodawanie":
    dodawanie(float(x),float(y))
elif operacja=="odejmowanie":
    odejmowanie(float(x),float(y))
else :
    print ("niewłaściwe argumenty","podaj:OPERACJA X Y")



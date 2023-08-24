# print("Hello")

"""
a = int(input())
b = int(input())
c = a+b
d = b-a
e = a*b
f = a//b
g = a/b
h = a%b
print(a,b,c,d,e,f,g,f,h)
"""

"""
word1 = ("Pustoye vi serdechnim ti")
word2 = ("Ona,obmolvyas,zamenila")
print(word1)
print(word2)
"""
"""
x = int(input())
y = int(input())
z = int(input())
f = (x*x)*((2*y)+(5*z))
print(f)

"""

"""
a = int(input())
b = hex(a)
print(b)
"""

"""
a = int(input())
b = format(a,"x")
print(b)
"""

"""
a = int(input("Vvedite chislo"))
digits = "0123456789ABCDEF"
number = ""
while a > 0:
    d = a % 16
    digit = digits[d]
    number = digit + number
    a //= 16
print("Shesnatirichnoe chislo:", number)
"""
#zadacha 2 glava 6
"""
s = [25,32,45,35,89]
a = len(s)
s.reverse()
print(a)
print(s)

"""
#zadacha 4 glava 6
"""
sinonims = {"Ugrumiy": "Holerik","Radostniy": "Veseliy","Bolesny": "Hvory","Otdihaty": "Raslablyatsya","Lodiry": "Bezdelnik","Narcoman": "Zavisimiy", "Oligator": "Crocodil","Bebemot":"Gipopotam", "Millioner": "Bogatiy","Voda": "Jitcost", "Seyf": "Hranilishe"}
print(sinonims)
"""
# zADACHA 1 GLADA 7
"""
a = ord("s")
b = ord("a")
c = ord("m")
d = ord("p")
e = ord("l")
f = ord("e")
print(a + b + c + d + e + f)
"""
# zadacha 2 glava 7
"""
a = 1
n = 2000
while a <= n:
    if a % 12 == 0 and a % 5 == 0:
        print(a)
    a += 1
"""
# Zadacha 3 glava 7
"""
a = int(input("Vvedite kilogramy :"))
b = 1
c = 0
while b <= a:
    c = c + 2.205
    b = b + 1
print("Skolko funtov :", c)

"""
"""
a = int(input("Vvedite kilogramy :"))
b = 1
c = 0
for b in range(a):
    c = c + 2.205
    b = b + 1
print("Skolko funtov :", c)
# Zadacha 4 glava 7
"""
"""
import random
print( random.randint(1000, 10000))
"""
# Zadacha 5 glava 7
"""
a = int(input("Vvedite skolko dollarov:"))
b = 1
c = 0
d = 0
while b <= a:
    c = c + 1.1
    d = d + 1.27
    b = b + 1
print("skolko euro:", c)
print("Skolko funtov:", d)
"""
"""
a = int(input("Vvedite nomer elementa ryada fibonachi:"))
fib1 = 1
fib2 = 1
i = 0
while i < a - 2:
    summ = fib1 + fib2
    fib1 = fib2
    fib2 = summ
    i = i + 1
print("Znachenie elementa fibonachi:", fib2)
"""

# Zadadcha 1 glava 8
"""
a = list(input().split(" "))
b = max(a)
print(b)
"""
# Zadach 2 glava 85
"""
a = list(input())
a.reverse()
print("perevernutiy spisok: ", a)
i = 0
c = 0
for i in range (len(a)):
    c = c + int(a[i])
    i = i + 1
print("Ssumma pervernutogo spiska: ", c)
"""
# Zadach 3 glava 8
"""
a = list(input())
b = list(input())
c = list(input())
a.reverse()
b.reverse()
c.reverse()
print(a)
print(b)
print(c)    
"""
# Zadacha 4 glava 8
"""
def recurs():
    a = 100
    b = 1
    c = 1
    while b <= a:
        c = c * b
        b = b + 1
    return(c)

print(recurs())
"""
# Zadacha 5 glava 8
"""
a = "This such a bad idea to bring u back home"
c = '..'
print(a.strip("i"))
print(a.replace("home", "life"))
print(a.split("b"))
c = c.join(a)
print(c)
"""
# Zadacha 7 glava 8
"""
a = "https://ru.wikipedia.org/wiki/Nissan_Tiida_(%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B5_%D0%BF%D0%BE%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)"
print("skopiruete ssilku:", a)
"""
# Zadacha 8 glava 8
"""
R = int(input())
G = int(input())
B = int(input())
if R == B and G == B and R == G:
    print("It's white")
elif R == 0 and G == 0 and B == 0:
    print("It's black")
elif R == B and G == 0:
    print("It's magenta")
elif G == B and R == 0:
    print("It's cyan")
elif G == R and  B == 0:
    print("It's yellow")
elif G == 0 and B == 0:
    print("It's red")
elif R == 0 and G == 0:
    print("It's blue")
elif R == 0 and B == 0:
    print("It's green")
"""

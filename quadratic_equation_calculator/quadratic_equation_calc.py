from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

def quadra_equa(a,b,c):
    if (a != 0):
        delta = b**2 - 4*a*c
        x1 = ((-1 * b) + sqrt(delta))/(2 * a)
        x2 = ((-1 * b) - sqrt(delta))/(2 * a)
        print(x1, x2)

print(quadra_equa(a,b,c))
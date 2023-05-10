# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número. 

num = int(input("Ingrese un numero: "))
calculo = 0
for i in range(1, num + 1, 1):
    calculo = calculo + i
    
print (calculo)
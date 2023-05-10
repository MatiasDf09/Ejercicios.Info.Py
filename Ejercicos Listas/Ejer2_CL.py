# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.
 
# Pido el numero al usurio 
num = int(input("Ingrese un numero: "))
calculo = 0
for i in range(1, num + 1, 1): # Bucle "For" que inicializa en 1 va hasta el n dado y va en 1 en 1 
    calculo = calculo + i      
   
 #  Mostramos el calculo aqui    
print (calculo)
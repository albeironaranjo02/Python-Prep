# Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y 
# luego imprimir por pantalla si es mayor o menor a cero

a = 10
if a > 0:
    print(f"{a} es mayor a 0")
else: print(f"{a} es menor a cero")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

a = 10
b = "10"
if type(a) == type(b):
    print(f"Las variables son del mismo tipo: {type(a)}")
else: print(f"Las variables osn de diferentes valor a es {type(a)} y b es {type(b)}")
# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range (11):
    if i % 2 == 0:
        print(f"{i} es par")
    else: print(f"{i} es impar")

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range (6):
    print(f"{i} a la 3 potencia es: {pow(i,3)}")

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

a = int(input("Digite un numero: "))
for i in range (a):
    print(f"Iteracion {i+1} de {a}")

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en
#  una variable, sólo si la variable contiene un número entero mayor a 0

num = int(input("Ingrese un numero para sacar el factorial:"))
factorial = 1
valor = 1
if num > 0:
    while valor <= num:
        factorial *= valor
        valor +=1
    print("El factorial de", num, "es", factorial)

else: print("Solo es posible para mayores a 1")

# 7) Crear un ciclo for dentro de un ciclo while
a = 8
iterador = 0
while iterador <= a:
    for i in range (a):
        if i == iterador:
            print (f"El iterador del while es igual al iterador del for")
    iterador += 1



# 8) Crear un ciclo while dentro de un ciclo for

for i in range (3):
    a=0
    while a < 3:
        print (f"Iterador del while menor al ietardor del rango 3")
        a += 1

# 9) Imprimir los números primos existentes entre 0 y 30

for i in range(1,31):
    cont = 0
    for j in range (1,i + 1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        print(f"{i} es un numero primo")


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores 
# divisibles por 12, dentro del rango de números de 100 a 300
a = 100
while a <=300:
    if a % 12 == 0:
        print(a, "Es divisible por 12")
    a +=1


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

a = 100 
while a <=300:
    if a % 3 == 0 and type(a // 6) == int :
        print(f"{a} Primer numero entre 100 y 300, que es divisible en tres y multiplo de 6")
        break
    a += 1

# ---- Actividad 1 ----
for i in range(100+1):
    print(i)


# ---- Actividad 2 ----
numero = input("Ingrese un numero entero:").strip()
while not numero.isdigit():
    print("ERROR: El numero ingresado no es valido")
    numero = input("Ingrese un numero entero:").strip()

numero = int(numero)
contador = 0
if numero < 0:
    numero *= -1
elif numero == 0:
    contador = 1

while numero != 0:
    numero = numero // 10
    contador += 1

print(f"El numero tiene {contador} digitos")


# ---- Actividad 3 ----
print("Sumador de intervalos abiertos de números")
inicio = input("Ingrese número de inicio:").strip()
while not inicio.isdigit():
    inicio = input("Ingrese número de inicio:").strip()
inicio = int(inicio)

fin = input("Ingrese número de fin:")
while not fin.isdigit():
    print("ERROR: El numero ingresado no es valido")
    fin = input("Ingrese número de fin:")
fin = int(fin)

acumulador = 0
for i in range(inicio+1, fin):
    acumulador += i

print(f"El total de la suma del intervalo ({inicio}; {fin}) es:", acumulador)


# ---- Actividad 4 ----
numero = -1
acumulador = 0

while numero != 0:
    while True:
        numero = input("Ingrese un numero (0 para finalizar):")
        if not numero.isdigit():
            print("ERROR: El numero ingresado no es valido")
        else: break
    numero = int(numero)
    if numero != 0:
        acumulador += numero

print("Total acumulado:", acumulador)


# ---- Actividad 5 ----
import random

numero_secreto = random.randrange(0, 9+1) and 0
intentos = 0
numero = -1

print("Adivine el numero secreto!")
print("Pista: el numero secreto esta entre el 0 y el 9 inclusive")
while numero != numero_secreto:
    if intentos > 0:
        print("Ese no es el numero... intente otra vez!")
    while True:
        numero = input("Ingrese un numero: ")
        if not numero.isdigit():
            print("ERROR: El numero ingresado no es valido")
        else: break
    numero = int(numero)

    intentos += 1

print("Adivinaste el numero!")
print(f"Intentaste adivinar {intentos} {intentos == 1 and 'vez' or 'veces'}")


# ---- Actividad 6 ----
for i in range(100+1, 0, -1):
    # Si el numero es par...
    if i % 2 == 0:
        print(i) # ...mostrarlo


# ---- Actividad 7 ----
acumulado = 0

fin = 0
while True:
    fin = input("Ingrese el numero maximo a iterar:").strip()
    if not fin.isdigit():
        print("ERROR: El numero ingresado no es valido")
    else: break
fin = int(fin)

for i in range(0, fin+1):
    acumulado += i

print(f"La suma de todos los numeros entre [0; {fin}] es:", acumulado)


# ---- Actividad 8 ----
# Contadores de números que cumplen las condiciones
cont_pares = 0
cont_impares = 0
cont_negativos = 0
cont_positivos = 0

LIMITE = 100

for i in range(LIMITE):
    numero = input(f"Ingrese un numero ({i+1} de {LIMITE}):")
    while not (numero.isdigit() or (numero.startswith("-") and numero[1:].isdigit())):
        print("ERROR: El numero ingresado no es valido")
        numero = input(f"Ingrese un numero ({i+1} de {LIMITE}):")
    numero = int(numero)

    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
    
    if numero > 0:
        cont_positivos += 1
    elif numero != 0:
        cont_negativos += 1


print("---- Resultados ----")
print("De los 100 numeros que se ingresaron hay...")
print(cont_pares, "numeros pares")
print(cont_impares, "numeros impares")
print(cont_negativos, "numeros negativos")
print(cont_positivos, "numeros positivos")


# ---- Actividad 9 ----

LIMITE = 100
acumulador = 0

for i in range(LIMITE):
    numero = input(f"Ingrese un numero ({i+1} de {LIMITE}):")
    while not numero.isdigit() and not (numero.startswith("-") and numero[1:].isdigit()):
        print("ERROR: El numero ingresado es invalido")
        numero = input(f"Ingrese un numero ({i+1} de {LIMITE}):")
    numero = int(numero)

    acumulador += numero


media = acumulador / LIMITE

print("La media de todos los numeros es:", media)


# ---- Actividad 10 ----
numero = input("Ingrese un número:")
while not numero.isdigit():
    print("ERROR: El numero ingresado no es valido")
    numero = input("Ingrese un número:")
numero = int(numero)

numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", numero_invertido)
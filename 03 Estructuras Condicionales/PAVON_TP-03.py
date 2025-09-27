# ----- Actividad 1 -----
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# ----- Actividad 2 -----
nota = int(input("Ingrese la nota obtenida: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ----- Actividad 3 -----
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# ----- Actividad 4 -----
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Usted es un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un/a adulto/a joven")
else:
    print("Usted es un/a adulto/a")

# ----- Actividad 5 -----
contraseña = input("Ingrese la contraseña: ")
longitud_contraseña = len(contraseña)
if longitud_contraseña >= 8 and longitud_contraseña <= 14:
    print("Ha ingresado la contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ----- Actividad 6 -----
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Para los valores", numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo o distribucion simetrica")
else:
    print("Analisis no concluyente")

# ----- Actividad 7 -----
frase = input("Ingrese una frase o palabra:")

if frase[-1] in "aeiou":
    frase += "!"
print(frase)

# ----- Actividad 8 -----
nombre = input("Ingrese su nombre;")
print("Ingrese una opcion para...")
print("1. Convertir su nombre en MAYÚSCULAS")
print("2. Convertir su nombre en minúsculas")
print("3. Convertir la primer letra de su nombre a Mayúsculas")
opcion = int(input("Opcion:"))

if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()
print("Resultado:", nombre)

# ----- Actividad 9 -----
magnitud = int(input("Ingrese la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4: 
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
else:
    # La magnitud es mayor o igual que 7
    print("Extremo")

# ---- Actividad  10 -----
hemisferio = input("En que hemisferio se encuentra? (N=Norte, S=Sur):").upper()
print()
if not (hemisferio == "N" or hemisferio == "S"):
    print("ERROR: El hemisferio ingresado no es valido")
else:
    # ----- AÑO -----
    año = int(input("Ingrese año:"))
    print()

    if año < 1:
        print("ERROR: El año es invalido")
    else:
        # ----- MES -----
        print("1. Enero")
        print("2. Febrero")
        print("3. Marzo")
        print("4. Abril")
        print("5. Mayo")
        print("6. Junio")
        print("7. Julio")
        print("8. Agosto")
        print("9. Septiembre")
        print("10. Octubre")
        print("11. Noviembre")
        print("12. Diciembre")
        mes = int(input("Ingrese numero del mes:"))
        print()

        if mes < 1 or mes > 12:
            print("ERROR: El mes ingresado no es valido")
        else:
            dia_maximo = 0
            if mes == 2:
                # --- Calculo del año bisiesto ----

                # El año se considera bisiesto cuando:
                # - Es divisible por 4 y...
                # - NO es divisible por 100
                # Caso contrario se comprueba si el año:
                # - Es divisible por 400
                if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
                    dia_maximo = 29
                else:
                    # Si ninguno de los casos es cierto
                    # entonces el año NO es bisiesto
                    dia_maximo = 28
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                # Los meses Abril, Junio, Septiembre y Noviembre tienen 30 dias
                dia_maximo = 30
            else:
                # Mientras que los meses restantes tienen 31
                dia_maximo = 31


            # ----- DIA -----
            dia = int(input(f"Ingrese el dia (entre 1 y {dia_maximo} inclusive):"))
            print()
    
            if dia < 1 or dia > dia_maximo:
                print("ERROR: El dia ingresado es invalido")
            else:
                print("Usted se encuentra en la estacion de", end=" ")

                # Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
                if (
                    (mes == 12 and dia >= 21) or 
                    (mes == 1) or
                    (mes == 2) or
                    (mes == 3 and dia <= 20)
                ):
                    if hemisferio == "N": print("Invierno")
                    elif hemisferio == "S": print("Verano")

                # Desde el 21 de marzo hasta el 20 de junio (incluidos)
                elif (
                    (mes == 3 and dia >= 21) or
                    (mes == 4) or
                    (mes == 5) or
                    (mes == 6 and dia <= 20 )
                ):
                    if hemisferio == "N": print("Primavera")
                    elif hemisferio == "S": print("Otoño")

                # Desde el 21 de junio hasta el 20 de septiembre (incluidos)
                elif (
                    (mes == 6 and dia >= 21) or
                    (mes == 7) or
                    (mes == 8) or
                    (mes == 9 and dia <= 20)
                ):
                    if hemisferio == "N": print("Verano")
                    elif hemisferio == "S": print("Invierno")

                # Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
                elif (
                    (mes == 9 and dia >= 21) or
                    (mes == 10) or
                    (mes == 11) or
                    (mes == 12 and dia <= 20)
                ):
                    if hemisferio == "N": print("Otoño")
                    elif hemisferio == "S": print("Primavera")

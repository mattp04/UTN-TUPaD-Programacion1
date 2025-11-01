import math


def imprimir_hola_mundo():
    print("Hola Mundo!")


def saludar_usuario(nombre):
    return f"Hola {nombre}!"


def informacion_personal(nombre, apellido, edad, residencia):
    """Muestra un mensaje breve con los datos personales proporcionados"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):
    return math.pi * (radio**2)


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


def segundos_a_horas(segundos):
    return segundos / 3600


def tabla_multiplicar(numero):
    """Imprime en consola, la tabla de multiplicar del 1 al 10 del numero proporcionado"""
    for i in range(1, 10 + 1):
        print(f"{numero}x{i}={numero*i}")


def operaciones_basicas(a, b):
    """
    Realiza suma, resta, multiplicacion y division
    de los numeros a y b recibidos por parámetro

    Retorna:
        Resultados de las operaciones en el siguiente orden: (suma, resto, producto, cociente)
    """
    suma = a + b
    resto = a - b
    producto = a * b
    cociente = a / b

    return (suma, resto, producto, cociente)


def calcular_imc(peso, altura):
    """
    Calcula el Indice de Masa Corporal utilizando el peso (en kilogramos) y la altura (en metros)

    Retorna:
        El indice de masa corporal
    """
    return peso / (altura**2)


def celsius_a_fahrenheit(celsius):
    return (1.8 * celsius) + 32


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


def main():
    print("\n\n----- 1. Hola Mundo -----")
    imprimir_hola_mundo()


    print("\n\n----- 2. Saludar usuario -----")
    nombre = input("¿Cuál es su nombre? ")
    saludar_usuario(nombre)


    print("\n\n----- 3. Informacion personal -----")
    apellido = input("¿Cuál es su apellido? ")
    edad = input("¿Cuantos años tiene? ")
    residencia = input("¿En que provincia y/o localidad se encuentra actualmente? ")
    informacion_personal(nombre, apellido, edad, residencia)


    print("\n\n----- 4. Calcular area y perimetro de un circulo -----")
    radio = int(input("Ingrese el radio de un circulo: "))
    print("El area del circulo es: ", calcular_area_circulo(radio))
    print("El perimetro del circulo es: ", calcular_perimetro_circulo(radio))


    print("\n\n----- 5. Segundos a horas -----")
    segundos = int(input("Ingrese segundos para convertir a horas: "))
    print(f"[!] {segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")


    print("\n\n----- 6. Tabla de multiplicar -----")
    numero = int(input("Ingrese el numero de la tabla a mostrar: "))
    tabla_multiplicar(numero)


    print("\n\n----- 7. Operaciones basicas -----")
    a = int(input("Ingrese numero a: "))
    b = int(input("Ingrese numero b: "))

    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {a}+{b} = {suma}")
    print(f"Resta: {a}-{b} = {resta}")
    print(f"Multiplicación: {a}x{b} = {mult}")
    print(f"Division: {a}/{b} = {div}")


    print("\n\n----- 8. Calcular IMC -----")
    peso = float(input("Ingrese su peso (en kilogramos): "))
    altura = float(input("Ingrese su altura (en metros): "))
    imc = calcular_imc(peso, altura)
    print(f"[!] Su Indice de Masa Corporal es: {imc}")


    print("\n\n----- 9. Temperatura de Celsius a Fahrenheit -----")
    grados_celsius = float(input("Ingrese una temperatura (en Celsius): "))
    print(
        f"[!] {grados_celsius}°C equivalen a {celsius_a_fahrenheit(grados_celsius)}°F"
    )

    print("\n\n----- 10. Calcular promedio notas -----")
    notas = []
    for i in range(3):
        nota = int(input(f"Ingrese una nota ({i} de 3):" ))
        notas.append(nota)

    promedio = calcular_promedio(*notas)
    print(f"[!] El promedio de las tres notas es: {promedio}")
    

main()

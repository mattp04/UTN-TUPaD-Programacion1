# Actividad 1
print("Hola Mundo")


# Actividad 2
nombre = input("Ingrese su nombre:")
print(f"Hola, {nombre}")


# Actividad 3
nombre = input("Nombre:")
apellido = input("Apellido:")
edad = int(input("Edad:"))
lugar_residencia = input("Lugar de residencia:")

nombre_completo = nombre + " " + apellido
print(f"Soy {nombre_completo}, tengo {edad} años y vivo en {lugar_residencia}")


# Actividad 4
PI = 3.1416
radio = float(input("Ingrese el radio de un circulo:"))
area = PI * (radio**2)
print("El area del circulo es:", area)


# Actividad 5
segundos = float(input("Ingrese la cantidad de segundos:"))
minutos = segundos / 60
horas = minutos / 60
print(f"{segundos} segundos equivale a {horas} horas")


# Actividad 6
num = int(input("Tabla de multiplicar a mostrar:"))
print(f"{num} x 0 = {num*0}")
print(f"{num} x 1 = {num*1}")
print(f"{num} x 2 = {num*2}")
print(f"{num} x 3 = {num*3}")
print(f"{num} x 4 = {num*4}")
print(f"{num} x 5 = {num*5}")
print(f"{num} x 6 = {num*6}")
print(f"{num} x 7 = {num*7}")
print(f"{num} x 8 = {num*8}")
print(f"{num} x 9 = {num*9}")
print(f"{num} x 10 = {num*10}")


# Actividad 7
numero1 = float(input("Ingrese el primer numero:"))
numero2 = float(input("Ingrese el segundo numero"))

print(f"Suma: {numero1} + {numero2} = {numero1+numero2}")
print(f"Resta: {numero1} - {numero2} = {numero1-numero2}")
print(f"Multiplicación: {numero1} * {numero2} = {numero1*numero2}")
print(f"Division: {numero1} / {numero2} = {numero1/numero2}")


# Actividad 8
altura = float(input("Ingrese su altura en metros:"))
peso = float(input("Ingrese su peso en kilogramos:"))
imc = peso / (altura**2)
print("Su Indice de Masa Corporal es:", imc)


# Actividad 9
celsius = float(input("Ingrese temperatura en grados Celsius: "))

fahrenheit = (9/5 * celsius) + 32
print("La temperatura en grados Fahrenheit es:", fahrenheit)


# Actividad 10
print("Promedio de 3 numeros")
a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
c = int(input("Ingrese el tercer numero:"))

promedio = (a+b+c) / 3
print("El promedio es:", promedio)
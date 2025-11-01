# ----- Ejercicio 1 -----
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# ----- Ejercicio 2 -----

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# ----- Ejercicio 3 -----

# Nombres de las frutas sin los precios
frutas = list(precios_frutas.keys())


# ----- Ejercicio 4 -----
contactos = {}

for i in range(5):
    print(f"----- Contacto {i+1} de 5) -----")
    nombre = input("Ingrese nombre del contacto: ")
    telefono = input("Ingrese numero de telefono del contacto: ")
    contactos[nombre] = telefono
print("[!] Registro finalizado\n")

nombre_solicitado = input("Ingrese nombre de contacto a buscar: ")
if nombre_solicitado in contactos:
    nombre = nombre_solicitado
    telefono = contactos[nombre]
    print("[!] Usuario encontrado")
    print("Nombre", nombre)
    print("Telefono:", telefono)
else:
    print("[!] Contacto inexistente")


# ----- Ejercicio 5 -----

frase = input("Ingrese una frase:")
palabras = frase.split()
palabras_unicas = set(palabras)

recuento_palabras = {}
for p in palabras:
    recuento_palabras[p] = recuento_palabras.get(p, 0) + 1

print("Palabras unicas:", palabras_unicas)
print("Recuento:", recuento_palabras)


# ----- Ejercicio 6 -----
alumnos = {}
for i in range(3):
    print(f"----- Alumno {i+1} de 3 -----")
    nombre = input("Ingrese nombre del alumno: ")
    while nombre in alumnos:
        print(f'ERROR: El alumno con nombre "{nombre}" ya ha sido ingresado')
        nombre = input("Ingrese nombre del alumno: ")
    notas = []
    for i in range(3):
        notas.append(int(input(f"Ingrese la nota N°{i+1}: ")))

    alumnos[nombre] = tuple(notas)
    print()

# Mostrar notas y promedio de notas de los alumnos
print()
for nombre in alumnos:
    print(f"----- Notas de {nombre} -----")
    notas = alumnos[nombre]
    for i in range(3):
        print(f"Nota N°{i+1}: {notas[i]}")
    print("Promedio:", sum(notas) / 3)
    print()


# ----- Ejercicio 7 -----

parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7}

# Los que aprobaron ambos parciales
ambos = parcial_1.intersection(parcial_2)

# Los que aprobaron solo uno
solo_uno = parcial_1.symmetric_difference(parcial_2)

# Los que aprobaron al menos uno (sin repetir)
al_menos_uno = parcial_1.union(parcial_2)

print("Ambos:", ambos)
print("Solo uno:", solo_uno)
print("Al menos uno:", al_menos_uno)


# ----- Ejercicio 8 -----

productos = {}
opcion = ""
while opcion != "0":
    print("----- Menu -----")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("0. Salir")
    opcion = input("Seleccione una opcion: ").strip()

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in productos:
            print(f"[!] Stock de {producto}: {productos[producto]}")
        else:
            print(f"ERROR: El producto {producto} no existe en el inventario")

    elif opcion == '2':
        producto = input("Ingrese el nombre del producto para agregar stock: ")
        if producto in productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            productos[producto] += cantidad
            print(f"[!] Stock de {producto} agregado correctamente. Nuevo stock: {productos[producto]}")
        else:
            print(f"ERROR: El producto {producto} no existe en el inventario")

    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto in productos:
            print(f"ERROR: El producto {producto} ya existe en el inventario")
        else:
            cantidad = int(input("Ingrese la cantidad inicial de stock: "))
            productos[producto] = cantidad
            print(f"[!] Producto {producto} agregado con stock {cantidad}")

    elif opcion == '0':
        print("[!] Saliendo del programa")
    else:
        print("ERROR: Opcion invalida")

    print()


# ----- Ejercicio 9 -----

agenda = {
    (1, 9): "Desayuno",
    (1, 12): "Clase de matemáticas",
    (1, 15): "Estudio en biblioteca",
    (4, 10): "Reunión con grupo de programación",
    (10, 14): "Juntada con amigos",
    (12, 8): "Clase de física",
}
dia = int(input("Ingrese el dia (1-31): "))
hora = int(input("Ingrese la hora (0-23): "))
evento = agenda.get((dia, hora), None)
if evento:
    print(f"[!] El dia {dia} a las {hora}:00 tiene el siguiente evento: {evento}")
else:
    print(f"[!] No hay eventos programados para el dia {dia} a las {hora}:00")


# ----- Ejercicio 10 -----
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima',
    'Venezuela': 'Caracas',
    'Uruguay': 'Montevideo',
}

print("[!] Diccionario paises -> capitales:", paises_capitales)

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("[!] Diccionario capitales -> paises:", capitales_paises)
# ----- EJERCICIO 1 -----
notas = [7, 8, 9, 7, 8, 6, 10, 8, 9, 8]
suma_notas = 0
promedio = 0
nota_alta = float("-inf")
nota_baja = float("inf")

for i in range(len(notas)):
    nota = notas[i]
    print(f"Nota Alumno Nro {i}: {nota}")
    suma_notas += nota
    if nota > nota_alta:
        nota_alta = nota
    if nota < nota_baja:
        nota_baja = nota

promedio = suma_notas / len(notas)

print()
print(f"Promedio notas: {promedio}")
print("La nota mas alta es:", nota_alta)
print("La nota mas baja es:", nota_baja)


# ----- EJERCICIO 2 -----
productos = []
for i in range(5):
    nombre_producto = input(f"Ingrese nombre producto ({i + 1} de 5): ").strip()
    while len(nombre_producto) == 0:
        print("ERROR: El nombre del producto no debe quedar vacio")
        nombre_producto = input("Ingrese nombre producto: ").strip()

    productos.append(nombre_producto)

productos.sort()
print()
print("[!] Mostrando listado de productos:")
for p in productos:
    print("-", p)

opcion = 0
while opcion != 3:
    print("-" * 20)
    print("1- Eliminar")
    print("2- Actualizar")
    print("3- Salir")

    opcion = input("Ingrese una opción: ").strip()
    while not opcion.isdecimal():
        print("ERROR: El numero ingresado no es valido")
        opcion = input("Ingrese una opción: ").strip()

    opcion = int(opcion)

    if opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ").strip()
        while len(nombre_producto) == 0:
            print("ERROR: El nombre del producto no debe quedar vacio")
            nombre_producto = input("Ingrese nombre producto").strip()

        if nombre_producto in productos:
            productos.remove(nombre_producto)
            print(f'[!] Nombre "{nombre_producto}" eliminado correctamente')
        else:
            print("ERROR: El nombre del producto ingresado no existe")

    elif opcion == 2:
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        while len(nombre_producto) == 0:
            print("ERROR: El nombre del producto no debe quedar vacio")
            nombre_producto = input("Ingrese nombre producto").strip()

        if nombre_producto in productos:
            indice_producto = productos.index(nombre_producto)
            print(f'[!] Producto encontrado "{nombre_producto}"')
            nuevo_nombre = input("Ingrese el nuevo nombre del producto:")
            productos[indice_producto] = nuevo_nombre
            print(
                f'[!] Nombre actualizado correctamente: "{nombre_producto}" -> "{nuevo_nombre}"'
            )
        else:
            print("ERROR: El nombre del producto ingresado no existe")
    elif opcion == 3:
        print("[!] Saliendo...")
    else:
        print("ERROR: Opción invalida")

productos.sort()
print()
print("[!] Mostrando productos despues de eliminar y/o actualizar:")
for p in productos:
    print("-", p)


# ----- EJERCICIO 3 -----
import random

numeros_pares = []
numeros_impares = []

for i in range(15):
    num = random.randint(1, 100)
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

cant_pares = len(numeros_pares)
cant_impares = len(numeros_impares)


print("[!] Mostrando numeros obtenidos:")
print(f"- Numeros Pares (cantidad: {cant_pares}): ", end="")
for i in range(cant_pares):
    n = numeros_pares[i]
    print(n, end="")
    if i != (cant_pares - 1):
        print(", ", end="")

print()

print(f"- Numeros Impares (cantidad: {cant_impares}): ", end="")
for i in range(cant_pares):
    n = numeros_pares[i]
    print(n, end="")
    if i != (cant_pares - 1):
        print(", ", end="")


# ----- EJERCICIO 4 -----
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
cant_datos = len(datos)

sin_repetidos = []

print("Datos iniciales: ", end="")
for i in range(cant_datos):
    print(datos[i], end="")
    if i != cant_datos - 1:
        print(", ", end="")
print()

for n in datos:
    if n not in sin_repetidos:
        sin_repetidos.append(n)

cant_sin_repetidos = len(sin_repetidos)
print("Lista sin elementos repetidos: ", end="")
for i in range(cant_sin_repetidos):
    print(sin_repetidos[i], end="")
    if i != cant_sin_repetidos - 1:
        print(", ", end="")
print()


# ----- EJERCICIO 5 -----
CANTIDAD_DE_ESTUDIANTES = 8
estudiantes_presentes = []

for i in range(CANTIDAD_DE_ESTUDIANTES):
    nombre_estudiante = input(
        f"Ingrese nombre de un estudiante presente ({i + 1} de {CANTIDAD_DE_ESTUDIANTES}):"
    ).strip()
    while len(nombre_estudiante) == 0:
        print("ERROR: El nombre no debe quedar vacio")
        nombre_estudiante = input(
            f"Ingrese nombre de un estudiante presente ({i + 1} de {CANTIDAD_DE_ESTUDIANTES}):"
        ).strip()

    estudiantes_presentes.append(nombre_estudiante)

print()
print("----- Listado de estudiantes -----")
for estudiante in estudiantes_presentes:
    print("-", estudiante)

opcion = -1
while opcion != 0:
    print("1- Agregar nuevo estudiante")
    print("2- Eliminar estudiante existente")
    print("0- Salir")

    opcion = input("Ingrese una opción:").strip()
    while not opcion.isdecimal():
        print("ERROR: EL valor ingresado no es un numero valido")
        opcion = input("Ingrese una opción:")

    opcion = int(opcion)
    if opcion == 0:
        print("Saliendo...")
    elif opcion == 1:
        nombre_estudiante = input("Ingrese el nombre del nuevo estudiante: ").strip()
        while len(nombre_estudiante) == 0:
            print("ERROR: El nombre no debe quedar vacio")
            nombre_estudiante = input(
                "Ingrese el nombre del nuevo estudiante: "
            ).strip()

        if nombre_estudiante not in estudiantes_presentes:
            estudiantes_presentes.append(nombre_estudiante)
            print(f'[!] Estudiante "{nombre_estudiante}" agregado correctamente')
        else:
            print(f'ERROR: El estudiante "{nombre_estudiante}" ya existe')

    elif opcion == 2:
        nombre_estudiante = input("Ingrese el nombre del nuevo estudiante: ").strip()
        while len(nombre_estudiante) == 0:
            print("ERROR: El nombre no debe quedar vacio")
            nombre_estudiante = input(
                "Ingrese el nombre del nuevo estudiante: "
            ).strip()
        if nombre_estudiante in estudiantes_presentes:
            estudiantes_presentes.remove(nombre_estudiante)
            print(f'[!] Estudiante "{nombre_estudiante}" eliminado correctamente')
        else:
            print(f'ERROR: El estudiante "{nombre_estudiante}" no existe')
    else:
        print("ERROR: Opción invalida")

    print("\n" + "-" * 20)


print("----- Listado de estudiantes FINAL -----")
for estudiante in estudiantes_presentes:
    print("-", estudiante)


# ----- EJERCICIO 6 -----
lista_numeros = [10, 20, 30, 40, 50, 60, 70]
print("----- Lista original -----")
for n in lista_numeros:
    print("-", n)

ultimo_elemento = lista_numeros.pop()

# Inserta el ultimo elemento al principio de la lista,
# causando que todos los elementos se desplacen una posición a la derecha
lista_numeros.insert(0, ultimo_elemento)

print()
print("----- Lista rotada -----")
for n in lista_numeros:
    print("-", n)


# ----- EJERCICIO 7 -----

# Cada fila interna es la temperatura [min, max] de un dia de la semana
temperaturas = [
    [10, 20],  # 0: Lunes
    [12, 22],  # 1: Martes
    [8, 18],  # 2: Miercoles
    [11, 21],  # 3: Jueves
    [13, 25],  # 4: Viernes
    [15, 26],  # 5: Sabado
    [14, 23],  # 6: Domingo
]

acum_maxima = 0
acum_minima = 0

amplitud_termica_maxima = float("-inf")
dia_mayor_amplitud_termica = ""

nro_de_semanas = len(temperaturas)
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("----- Temperatura de la semana -----")
for i in range(nro_de_semanas):
    dia = dias_semana[i]
    min, max = temperaturas[i]
    acum_maxima += max
    acum_minima += min
    amplitud_termica = max - min

    print(f"- {dia} (Amplitud termica: {amplitud_termica})")
    print(f" Maxima: {max}°C")
    print(f" Minima: {min}°C")
    print()

    if amplitud_termica > amplitud_termica_maxima:
        amplitud_termica_maxima = amplitud_termica
        dia_mayor_amplitud_termica = dia

promedio_maxima = acum_maxima / nro_de_semanas
promedio_minima = acum_minima / nro_de_semanas

print(f"Promedio temperatura máxima: {promedio_maxima}°C")
print(f"Promedio de temperatura minima: {promedio_minima}°C")
print(f"El dia {dia_mayor_amplitud_termica} es el de mayor amplitud termica")
print(f"Con {amplitud_termica_maxima} de amplitud termica")


# ----- EJERCICIO 8 -----
CANTIDAD_MATERIAS = 3
# Filas: Estudiantes
# Columnas: Matematicas, Fisica, Biologia
notas_estudiantes = [
    [8, 7, 9],
    [9, 9, 10],
    [7, 7, 8],
    [10, 9, 8],
    [7, 6, 7],
]

cantidad_estudiantes = len(notas_estudiantes)

promedios_alumnos = []
promedios_materias = []
acumulador_materias = []

# Inicializar acumulador_materias
for i in range(CANTIDAD_MATERIAS):
    acumulador_materias.append(0)

for i in range(cantidad_estudiantes):
    acumulador = 0
    for j in range(CANTIDAD_MATERIAS):
        nota = notas_estudiantes[i][j]
        acumulador += nota
        acumulador_materias[j] += nota

    promedios_alumnos.append(acumulador / CANTIDAD_MATERIAS)

for i in range(CANTIDAD_MATERIAS):
    promedios_materias.append(acumulador_materias[i] / cantidad_estudiantes)


print("----- Notas estudiantes -----")
for i in range(cantidad_estudiantes):
    notas = notas_estudiantes[i]
    print(f"- Estudiante N°{i + 1}")
    print(f"  Matemáticas: {notas[0]}")
    print(f"  Física: {notas[1]}")
    print(f"  Biología: {notas[2]}")

    prom = promedios_alumnos[i]
    print(f"  Promedio: {prom}")
    print("")

print()
print("----- Promedios de notas por materia -----")
print(f"Matemáticas: {promedios_materias[0]}")
print(f"Física: {promedios_materias[1]}")
print(f"Biología: {promedios_materias[2]}")


# ----- EJERCICIO 9 -----

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

posibles_combinaciones = [
    # Filas
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    # Columnas
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    # Diagonal
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
]

es_turno_jugador_1 = True
juego_finalizado = False
ganador = ""
ficha = "X" if es_turno_jugador_1 else "O"

while not juego_finalizado:
    # Mostrar tablero con fichas colocadas
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(f" {tablero[i][j]} ", end="│")
            else:
                print(f" {tablero[i][j]} ")
        if i < 2:
            print("───┼───┼───")
    print("-" * 20)

    # Mostrar tablero con numeros en los casilleros
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(f" {i * 3 + j + 1} ", end="│")
            else:
                print(f" {i * 3 + j + 1} ")
        if i < 2:
            print("───┼───┼───")

    # Solicitar casillero a colocar ficha
    ficha = "X" if es_turno_jugador_1 else "O"
    casillero_a_colocar = input(
        f"Ingrese numero de casillero a colocar la {ficha} (del 1 al 9): "
    ).strip()

    while (
        not casillero_a_colocar.isdigit()
        or int(casillero_a_colocar) < 1
        or int(casillero_a_colocar) > 9
    ):
        print("ERROR: El numero ingresado no es valido")
        casillero_a_colocar = input(
            f"Ingrese numero de casillero a colocar la {ficha} (del 1 al 9): "
        ).strip()

    casillero_a_colocar = int(casillero_a_colocar) - 1
    fila = (casillero_a_colocar // 3) % 3
    columna = casillero_a_colocar % 3

    # Comprobar si la casilla esta vacia
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = ficha

        # Comprobar si hay coincidencias por jugada
        combinacion_valida = True
        for combinacion in posibles_combinaciones:
            combinacion_valida = True
            for coordenadas in combinacion:
                x = coordenadas[0]
                y = coordenadas[1]
                # Verificar si se encuentra la ficha del jugador actual
                if tablero[x][y] != ficha:
                    combinacion_valida = False

            if combinacion_valida:
                break

        # Si hay coincidencia, levantar bandera para indicar que el juego ha finalizado
        # y guardar ficha del ganador
        if combinacion_valida:
            ganador = ficha
            juego_finalizado = True
        else:
            # caso contrario, alternar bandera para cambiar de turno
            es_turno_jugador_1 = not es_turno_jugador_1

        # Comprobar si hay espacio libre para el siguiente turno
        hay_espacio_libre = False
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == "-":
                    hay_espacio_libre = True

        # Caso contrario, marcar el levantar bandera para indicar que
        # el juego ha finalizado, sin asignar la variable ganador para
        # indicar que no hay ganadores
        if not hay_espacio_libre:
            juego_finalizado = True
    else:
        print("ERROR: Casillero ocupado por", tablero[fila][columna])
    print()


print("Juego finalizado")
if ganador:
    print(f"Ha ganado {ganador}!")
else:
    print("Empate")


# ----- EJERCICIO 10 -----

# Filas: Dias de la semana
# Columnas: Ventas 'Mouse', Ventas 'Teclado', Ventas 'Monitor', Ventas 'SSD'
ventas_semana = [
    [10, 5, 2, 8],
    [15, 6, 3, 10],
    [12, 8, 1, 11],
    [10, 10, 4, 14],
    [20, 15, 5, 20],
    [25, 18, 7, 22], 
    [22, 16, 4, 19], 
]

productos = ["Mouse", "Teclado", "Monitor", "SSD"]
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("----- Total vendido por cada producto -----")
totales_productos = [0, 0, 0, 0]

for dia in ventas_semana:
    for i in range(len(productos)):
        # Sumamos la venta de este producto (dia[i]) a su total (totales_productos[i])
        totales_productos[i] += dia[i]

for i in range(len(productos)):
    print(f"Total {productos[i]}: {totales_productos[i]} unidades")


print("\n----- Día con mayores ventas totales -----")
mayor_venta_diaria = float("-inf")
indice_mayor_venta_diaria = 0

for i in range(len(ventas_semana)):
    total_dia = 0
    ventas_dia = ventas_semana[i]
    for venta in ventas_dia:
        total_dia += venta
    if total_dia > mayor_venta_diaria:
        mayor_venta_diaria = total_dia
        indice_mayor_venta_diaria = i

print(
    f"El día con mayores ventas fue el dia {dias_semana[indice_mayor_venta_diaria]} con {mayor_venta_diaria} unidades vendidas."
)

print("\n----- Producto más vendido en la semana -----")
producto_mas_vendido = ""
max_unidades_vendidas = float("-inf")

for i in range(len(totales_productos)):
    if totales_productos[i] > max_unidades_vendidas:
        max_unidades_vendidas = totales_productos[i]
        producto_mas_vendido = productos[i]

print(
    f"El producto más vendido fue '{producto_mas_vendido}' con {max_unidades_vendidas} unidades."
)

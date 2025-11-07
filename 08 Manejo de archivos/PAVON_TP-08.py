NOMBRE_ARCHIVO = "productos.txt"


def inicializar_archivo():
    """
    Actividad 1: Crear archivo inicial con productos con el nombre 'productos.txt'
    """

    # Aseguramos que el archivo exista
    # Se abre en modo 'a' (append) .
    # Este modo crea el archivo si no existe, caso contrario abre el archivo manteniendolo intacto.
    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8"):
        pass  # En este caso, solo nos interesa que se cree el archivo

    # Verificamos si el archivo está vacío
    esta_vacio = False
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        # Leemos la primer linea, Si f.readline() devuelve Falso (osea una cadena vacía),
        # significa que el archivo no tiene contenido.
        primer_linea = f.readline()
        if not primer_linea:
            esta_vacio = True

    # Si estaba vacío, escribimos los datos iniciales
    if esta_vacio:
        print(f"[!] Agregando productos iniciales al archivo '{NOMBRE_ARCHIVO}'...")

        # Abrimos en modo 'w' (write) para escribir (sobrescribir)
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            # Lista de productos iniciales
            productos_iniciales = [
                "Lapicera,120.50,30\n",
                "Cuaderno,3520,15\n",
                "Regla,1100,25\n",
            ]
            f.writelines(productos_iniciales)

def extraer_productos_de_archivo(archivo):
    """
    Se extraen los productos de las lineas en el siguiente formato:
    (nombre, precio, cantidad)
    y se retorna una lista de ellas
    """

    productos = []
    for n_linea, linea in enumerate(archivo):
        # Usamos .strip() para limpiar saltos de línea
        linea_limpia = linea.strip()

        # Si es una linea vacia se sigue con la siguiente linea
        if not linea_limpia:
            continue

        # Validación de formato (debe tener 2 comas)
        if linea_limpia.count(",") != 2:
            print(f"[!] Error en la línea {n_linea + 1}:")
            print("\t->", linea_limpia)
            print(f"ERROR: No tiene el formato correcto. Se omitirá.")
            continue

        # Usamos .split(",") para separar los datos
        nombre, precio_str, cantidad_str = linea_limpia.split(",")

        # Validación de tipos de datos antes de convertir
        if not (precio_str.replace(".", "", 1).isdigit()):
            print(f"[!] Error en la línea {n_linea + 1}:")
            print("\t->", linea_limpia)
            print(f"ERROR: El precio '{precio_str}' no es un número. Se omitirá.")
            continue
        if not (cantidad_str.isdigit()):
            print(f"[!] Error en la línea {n_linea + 1}:")
            print("\t->", linea_limpia)
            print(
                f"Error: La cantidad '{cantidad_str}' no es un entero. Se omitirá."
            )
            continue

        precio = float(precio_str)
        cantidad = int(cantidad_str)

        productos.append((nombre, precio, cantidad))

    return productos


def leer_y_mostrar_productos():
    """
    Actividad 2: Muestra los productos de la lista con el siguiente formato:
    Producto: Lapicera | Precio: $120.50 | Cantidad: 30
    """
    # Abrimos el archivo en modo 'r' (read)
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        # Iteramos la lista e imprimimos con el formato
        productos = extraer_productos_de_archivo(f)
        print("\n--- Listado de Productos ---")
        for p in productos:
            # Se desempaquetan los valores
            nombre, precio, cantidad = p
            print(
                f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}"
            )
        print("----------------------------\n")


def agregar_producto():
    """
    Actividad 3: Agregar productos desde teclado.
    """
    print("\n--- Agregar Nuevo Producto ---")

    nombre = input("Ingrese nombre: ").strip()
    while not nombre:
        print("ERROR: El nombre no debe quedar vacio.")
        nombre = input("Ingrese nombre: ").strip()

    precio = input("Ingrese precio: ").strip()
    while not precio.replace(".", "", 1).isdigit() or float(precio) < 0:
        print("ERROR: Ingrese un precio valido (numero positivo y con un solo punto decimal si es necesario).")
        precio = input("Ingrese precio: ").strip()
    precio = float(precio)

    cantidad_str = input("Ingrese cantidad: ").strip()
    while not cantidad_str.isdigit() or int(cantidad_str) < 0:
        print("ERROR: Ingrese una cantidad válida (un número entero ej: 30).")
        cantidad_str = input("Ingrese cantidad: ").strip()
    cantidad = int(cantidad_str)

    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

    print(f"¡Producto '{nombre}' agregado a la lista!")


def cargar_productos():
    """
    Actividad 4: Cargar productos en una lista de diccionarios.
    Lee el archivo 'productos.txt' y retorna una lista.
    """
    productos = []  # Lista de diccionarios

    # Abrimos el archivo en modo 'r' (read)
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
        productos_extraidos = extraer_productos_de_archivo(f)
        for p in productos_extraidos:
            nombre, precio, cantidad = p

            # Creamos el diccionario
            producto_dict = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
            }
            productos.append(producto_dict)

    return productos


def buscar_producto(lista_productos):
    """
    Actividad 5: Buscar producto por nombre .
    """
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    while not nombre_buscar:
        print("ERROR: El nombre no debe quedar vacio.")
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    encontrado = False
    # Recorrer la lista de productos
    for p in lista_productos:
        # Comparamos en minúsculas para una búsqueda flexible
        if p["nombre"].lower() == nombre_buscar:
            print("\n¡Producto encontrado!")
            print(f"  Nombre: {p['nombre']}")
            print(f"  Precio: ${p['precio']:.2f}")
            print(f"  Cantidad: {p['cantidad']}")
            encontrado = True
            break  # Terminamos el bucle al encontrar el primero

    # Mostrar mensaje si no existe
    if not encontrado:
        print(f"ERROR: Producto '{nombre_buscar}' no encontrado.")


def guardar_productos(lista_productos):
    """
    Actividad 6: Guardar los productos actualizados .
    Sobrescribe el archivo 'productos.txt' con la lista actualizada.
    """
    print("\nGuardando productos en el archivo...")

    # Abrimos en modo 'w' (write) para sobrescribir
    # Esto logra la persistencia de los datos actualizados
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
        for p in lista_productos:
            # Convertimos el dict de nuevo al formato "nombre,precio,cantidad"
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("¡Productos guardados exitosamente!")


def main():
    inicializar_archivo()
    leer_y_mostrar_productos()
    agregar_producto()
    productos = cargar_productos()
    buscar_producto(productos)
    guardar_productos(productos)

# Punto de entrada del programa
if __name__ == "__main__":
    main()

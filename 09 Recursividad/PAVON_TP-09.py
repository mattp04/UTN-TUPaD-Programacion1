# ----- Ejercicio 1 -----
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i}: {factorial(i)}")


# ----- Ejercicio 2 -----
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese una posición para Fibonacci: "))

for i in range(num + 1):
    print(fibonacci(i), end=" ")


# ----- Ejercicio 3 -----
def potencia(base, expo):
    if expo == 0:
        return 1
    return base * potencia(base, expo - 1)

b = int(input("Base: "))
e = int(input("Exponente: "))
print("Resultado:", potencia(b, e))


# ----- Ejercicio 4 -----
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
print("Binario:", decimal_a_binario(num))


# ----- Ejercicio 5 -----
def es_palindromo(palabra):
    # Normalización mínima: quitar espacios y pasar a minúsculas.
    s = palabra.replace(" ", "").lower()
    # caso base: cadena vacía o un carácter
    if len(s) <= 1:
        return True
    # si los extremos no coinciden, no es palíndromo
    if s[0] != s[-1]:
        return False
    # caso recursivo: verificar los caracteres interiores de la palabra
    return es_palindromo(s[1:-1])

# Ejemplos:
print(es_palindromo("radar"))      # True
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False


# ----- Ejercicio 6 -----
def suma_digitos(n):
    n = abs(n)  # por si ingresan un numero negativo
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejemplos:
print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8


# ----- Ejercicio 7 -----
def contar_bloques(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplos:
print(contar_bloques(1))  # 1
print(contar_bloques(2))  # 3
print(contar_bloques(4))  # 10


# ----- Ejercicio 8 -----
def contar_digito(numero, digito):
    if digito < 0 or digito > 9:
        raise ValueError("El dígito debe estar entre 0 y 9.")
    numero = abs(numero)

    # caso especial: el número 0
    if numero == 0:
        return 1 if digito == 0 else 0

    # caso recursivo general
    if numero < 10:
        return 1 if numero == digito else 0

    # caso inicial
    inc = 1 if numero % 10 == digito else 0
    return inc + contar_digito(numero // 10, digito)

# Ejemplos:
print(contar_digito(12233421, 2))  # 3
print(contar_digito(5555, 5))      # 4
print(contar_digito(123456, 7))    # 0
print(contar_digito(0, 0))         # 1

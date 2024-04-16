import math

def biseccion(funcion, a, b, tolerancia=1e-10, max_iteraciones=1000):
    iteracion = 0
    while iteracion < max_iteraciones:
        c = (a + b) / 2
        if abs(funcion(c)) < tolerancia:
            return c, iteracion
        if funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c
        iteracion += 1
    return None, iteracion

def secante(funcion, x0, x1, tolerancia=1e-10, max_iteraciones=1000):
    iteracion = 0
    while iteracion < max_iteraciones:
        x2 = x1 - (funcion(x1) * (x1 - x0)) / (funcion(x1) - funcion(x0))
        if abs(x2 - x1) < tolerancia:
            return x2, iteracion
        x0 = x1
        x1 = x2
        iteracion += 1
    return None, iteracion

def newton_raphson(funcion, derivada, x0, tolerancia=1e-10, max_iteraciones=1000):
    iteracion = 0
    while iteracion < max_iteraciones:
        x1 = x0 - funcion(x0) / derivada(x0)
        if abs(x1 - x0) < tolerancia:
            return x1, iteracion
        x0 = x1
        iteracion += 1
    return None, iteracion

# Función y su derivada
def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

# Intervalo inicial para la bisección
a, b = 2, 3

# Punto inicial para la secante y Newton-Raphson
x0 = 2

# Encontrar la raíz usando cada método
raiz_biseccion, iteraciones_biseccion = biseccion(f, a, b)
raiz_secante, iteraciones_secante = secante(f, x0, x0 + 1)
raiz_newton_raphson, iteraciones_newton_raphson = newton_raphson(f, df, x0)

# Mostrar resultados
print("Método de la bisección:")
print("Raíz:", raiz_biseccion)
print("Iteraciones:", iteraciones_biseccion)

print("\nMétodo de la secante:")
print("Raíz:", raiz_secante)
print("Iteraciones:", iteraciones_secante)

print("\nMétodo de Newton-Raphson:")
print("Raíz:", raiz_newton_raphson)
print("Iteraciones:", iteraciones_newton_raphson)

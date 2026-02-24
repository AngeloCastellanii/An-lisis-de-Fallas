import math

print("--- 1. PUENTE GRU (Biseccion) ---")
def f1(x): return x**3 - 12*x - 101
a1, b1 = 1.0, 10.0
iteraciones = 0
xr_prev = 0
error_rel = 100.0

while True:
    iteraciones += 1
    xr = (a1 + b1) / 2
    if iteraciones > 1:
        error_rel = abs((xr - xr_prev) / xr) * 100
    if error_rel < 1.0 and iteraciones > 1:
        break
    if f1(a1) * f1(xr) < 0:
        b1 = xr
    else:
        a1 = xr
    xr_prev = xr

print(f"Raiz estimada (x): {xr:.4f}")
print(f"Iteraciones necesarias: {iteraciones}")


print("\n--- 2. CUATRICENTENARIO (Falsa Posicion) ---")
def f2(t): return 34 + (83 - 34) * math.exp(-0.077 * t) - 52
a2, b2 = 0.0, 100.0

# Iteración 1
t1 = b2 - (f2(b2) * (a2 - b2)) / (f2(a2) - f2(b2))
if f2(a2) * f2(t1) < 0:
    b2_new = t1
    a2_new = a2
else:
    a2_new = t1
    b2_new = b2

# Iteración 2
t2 = b2_new - (f2(b2_new) * (a2_new - b2_new)) / (f2(a2_new) - f2(b2_new))
error_aprox_it2 = abs((t2 - t1) / t2) * 100

# Raíz exacta (cálculo analítico para el tiempo final)
tiempo_calculado = -math.log(18/49) / 0.077

print(f"Tiempo calculado (t): {tiempo_calculado:.4f}")
print(f"Error APROXIMADO en Iteracion 2 (%): {error_aprox_it2:.4f}")


print("\n--- 3. TERMOZULIA (Newton-Raphson) ---")
def f3(x): return x**2 - 5 * math.log(x + 1) - 5
def df3(x): return 2*x - 5/(x + 1)

df3_en_2 = df3(2.0)

# Encontrar la raíz
x_n = 3.0 # Valor inicial
for _ in range(20):
    x_n = x_n - f3(x_n) / df3(x_n)

print(f"Reactancia critica (x): {x_n:.4f}")
print(f"Valor de f'(x) en x=2: {df3_en_2:.4f}")


print("\n--- 4. FALLA A TIERRA (Secante) ---")
def f4(R): return R * math.exp(0.1 * R) - 3.28
x0, x1 = 1.0, 1.5

# Siguiente x (Iteración 1 a partir de los valores dados)
x2 = x1 - f4(x1) * (x0 - x1) / (f4(x0) - f4(x1))

# Encontrar la raíz final
xa, xb = x0, x1
for _ in range(20):
    xc = xb - f4(xb) * (xa - xb) / (f4(xa) - f4(xb))
    xa, xb = xb, xc

print(f"Resistencia (R): {xb:.4f}")
print(f"Siguiente x (si x0=1, x1=1.5): {x2:.4f}")
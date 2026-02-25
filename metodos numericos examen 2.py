import math

print("--- 1. PUENTE GRU (Biseccion) ---")
def f1(x):
    return x**3 - 12*x - 101

a1, b1 = 1.0, 10.0
tol_biseccion = 1.0
iteraciones = 0
xr_prev = None
error_rel = float("inf")

while True:
    iteraciones += 1
    xr = (a1 + b1) / 2
    if xr_prev is not None and xr != 0:
        error_rel = abs((xr - xr_prev) / xr) * 100
    if xr_prev is not None and error_rel < tol_biseccion:
        break
    if f1(a1) * f1(xr) < 0:
        b1 = xr
    else:
        a1 = xr
    xr_prev = xr

print(f"Raiz estimada (x): {xr:.4f}")
print(f"Iteraciones necesarias (Error Relativo < {tol_biseccion:.0f}%): {iteraciones}")
print("Criterio de convergencia: Lineal")
print("Condicion de sub-intervalo: f(a)*f(xr) < 0")


print("\n--- 2. CUATRICENTENARIO (Falsa Posicion) ---")
def f2(t):
    return 34 + (83 - 34) * math.exp(-0.077 * t) - 52

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
print("Ventaja vs Biseccion: Aprovecha magnitud de f(x)")
print("Desventaja principal: Estancamiento unilateral")


print("\n--- 3. TERMOZULIA (Newton-Raphson) ---")
def f3(x):
    return x**2 - 5.06 * math.log(x + 1) - 5

def df3(x):
    return 2*x - 5.06/(x + 1)

df3_en_2 = df3(2.0)

# Encontrar la raíz
x_n = 3.0 # Valor inicial
for _ in range(50):
    derivada = df3(x_n)
    if abs(derivada) < 1e-14:
        break
    x_next = x_n - f3(x_n) / derivada
    if x_next != 0 and abs((x_next - x_n) / x_next) * 100 < 1.0:
        x_n = x_next
        break
    x_n = x_next

print(f"Reactancia critica (x): {x_n:.4f}")
print(f"Valor de f'(x) en x=2: {df3_en_2:.4f}")
print("Requisito critico: f'(x) debe existir y no ser cero")
print("Velocidad de convergencia: Cuadratica")


print("\n--- 4. FALLA A TIERRA (Secante) ---")
def f4(R):
    return R * math.exp(0.1 * R) - 3.28

x0, x1 = 1.0, 1.5
tol_secante = 1.0  # criterio de convergencia en porcentaje
max_iter_secante = 50

# Siguiente x (Iteración 1 a partir de los valores dados)
den_primera = f4(x0) - f4(x1)
if abs(den_primera) < 1e-14:
    x2 = x1
else:
    x2 = x1 - f4(x1) * (x0 - x1) / den_primera

# Encontrar la raíz final
xa, xb = x0, x1
iter_secante = 0
error_secante = float("inf")
motivo_paro = "Se alcanzo el maximo de iteraciones"

for _ in range(max_iter_secante):
    iter_secante += 1
    fxa = f4(xa)
    fxb = f4(xb)
    denominador = fxa - fxb

    if abs(denominador) < 1e-14:
        motivo_paro = "Denominador casi cero en la formula de secante"
        break

    xc = xb - fxb * (xa - xb) / denominador

    if xc != 0:
        error_secante = abs((xc - xb) / xc) * 100
    else:
        error_secante = abs(xc - xb) * 100

    xa, xb = xb, xc

    if error_secante < tol_secante:
        motivo_paro = "Convergencia alcanzada"
        break

print(f"Resistencia (R): {xb:.4f}")
print(f"Siguiente x (si x0=1, x1=1.5): {x2:.4f}")
print("Diferencia con Newton: No usa derivadas analiticas")
print("Riesgo numerico: Division por cero si f(xi) = f(xi-1)")
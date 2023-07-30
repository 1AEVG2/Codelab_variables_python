# Defenición de variables de cada tipo de primitivo
año = 2023
temperatura = 24.5
direccion = "Ecuador" 
llueve = False

print(f"{año}\n{temperatura}\n{direccion}\n{llueve}")

# Int: Los números enteros no tienen límite en Python.
# Float: Los números decimales no tienen un límite.
# Sin embargo hay ciertos casos en los que un ordenador no puede reconocer los números decimales ya que no son números reales.

# Ejercicio de la suma de los primeros n números pares.
def suma_primeros_n_pares(n):
    suma = n * (n + 1)
    return suma

n = int(input("Ingrese el valor de n (número entero): "))
resultado = suma_primeros_n_pares(n)
print(f"La suma de los primeros {n} números pares es: {resultado}")
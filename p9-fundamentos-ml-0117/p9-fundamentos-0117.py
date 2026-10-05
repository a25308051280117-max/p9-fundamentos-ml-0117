# 1. CREAR VARIABLES

x = 10
print(x)

nombre = "Matias"
print(nombre)

edad = 20
print(edad)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 2. CAMBIAR EL TIPO DE UNA VARIABLE

a = 5
a = "Hola"
print(a)

b = 10
b = 3.5
print(b)

c = "Python"
c = 100
print(c)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 3. CASTING

x = str(10)
print(x)

y = int("20")
print(y)

z = float(30)
print(z)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 4. OBTENER EL TIPO

x = 10
print(type(x))

nombre = "Juan"
print(type(nombre))

numero = 2.5
print(type(numero))

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 5. COMILLAS SIMPLES Y DOBLES

a = "Hola"
print(a)

b = 'Python'
print(b)

c = "Matias"
print(c)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 6. CASE-SENSITIVE

edad = 18
Edad = 20
EDAD = 25

print(edad)
print(Edad)
print(EDAD)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 7. VARIOS VALORES A VARIAS VARIABLES

x, y, z = 1, 2, 3
print(x, y, z)

a, b, c = "Rojo", "Verde", "Azul"
print(a, b, c)

nombre, edad, ciudad = "Ana", 18, "Juarez"
print(nombre, edad, ciudad)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 8. UN VALOR PARA VARIAS VARIABLES

x = y = z = 10
print(x, y, z)

a = b = c = "Hola"
print(a, b, c)

nombre = apellido = "Lopez"
print(nombre, apellido)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 9. DESEMPAQUETAR UNA COLECCIÓN

frutas = ["Manzana", "Banana", "Cereza"]
x, y, z = frutas
print(x, y, z)

numeros = [10, 20, 30]
a, b, c = numeros
print(a, b, c)

datos = ["Juan", 20, "Mexico"]
nombre, edad, pais = datos
print(nombre, edad, pais)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 10. OPERADORES ARITMÉTICOS

print(10 + 5)
print(10 - 5)
print(10 * 5)

print(10 / 2)
print(10 % 3)
print(2 ** 3)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 11. OPERADORES DE COMPARACIÓN

print(10 == 10)
print(10 != 5)
print(10 > 5)

print(5 < 10)
print(10 >= 10)
print(5 <= 10)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# 12. OPERADORES LÓGICOS

print(10 > 5 and 10 < 20)

print(10 > 20 or 10 < 20)

print(not(10 > 20))
print("Matias Lopez NC 0117")
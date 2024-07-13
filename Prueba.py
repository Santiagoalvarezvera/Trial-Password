import random

# Variable que contiene todos los caracteres posibles para la contraseña
caracteres_contrasena = "+-/*!&$#=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Pedir al usuario que introduzca la longitud de la contraseña
longitud = int(input("Introduce la longitud de la contraseña: "))

# Variable para almacenar la contraseña generada
contrasena_generada = ""

# Bucle para generar la contraseña
for _ in range(longitud):
    contrasena_generada += random.choice(caracteres_contrasena)

# Imprimir la contraseña generada
print("La contraseña generada es:", contrasena_generada)

# Pedir al usuario que introduzca la contraseña generada
contrasena_introducida = input("Introduce la contraseña generada: ")

# Verificar si la contraseña introducida es correcta
if contrasena_introducida == contrasena_generada:
    print("¡Contraseña correcta!")
else:
    print("Error: La contraseña introducida no es correcta.")

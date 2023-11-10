### Created by Ataik

import hashlib
while True:
    print("\n1. Codificar la contraseña en MD5")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        password = input("Ingrese la contraseña: ")

        md5_password = hashlib.md5(password.encode()).hexdigest()

        print("La contraseña codificada en MD5 es:", md5_password)

    elif opcion == "2":
        print("¡Hasta luego!")
        break


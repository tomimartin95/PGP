
# Imports
import random


# Generator
def password_generator():
    while True:
        try:
            length = int(input("\nPor favor, ingrese la longitud deseada de la contraseña:\n-> "))
            if length < 6:
                print("Es muy débil, pruebe con más caracteres")
                continue
            caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
            password = "".join(random.sample(caracters, length))
            return password
        
        except ValueError:
            print("Por favor, ingrese un número entero")

#! Password Generator Program (PGP)


# Imports
from greeting import greeting
from generator import password_generator


# Program
greeting()

contrasena_generada = password_generator()
print(f'\nTu nueva contraseña es: "{contrasena_generada}"\n')

# Imports
from generator import password_generator

# Password printer
def pass_print():
    
    contrasena_generada = password_generator()
    
    if contrasena_generada == None:
        pass
    
    else:
        print(f'\nTu nueva contraseña es: "{contrasena_generada}"\n')
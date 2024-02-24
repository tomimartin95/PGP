
# Imports
import random

# Generator
def password_generator():
    
    while True:
        request = input("Desea crear una nueva contraseña?\n1. Si  /  2. No\n-> ")
        
        if request == "1":
            
            while True:
                length = input("\nPor favor, ingrese la longitud deseada de la contraseña:\n-> ")
                
                while not length.isdigit():
                    length = input("\nERROR, coloque un número\n-> ")
                
                length = int(length)
                
                if length < 6:
                    print("Es muy débil, pruebe con más caracteres")
                    continue
                
                if length > 25:
                    print("Es muy larga, pruebe con menos caracteres")
                    continue
                
                caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
                password = "".join(random.sample(caracters, length))
                
                return password
            
        elif request == "2":
            print("\nFinalizando programa...")
            break
        
        else:
            print("\nOpción incorrecta, vuelva a intentarlo\n")
            continue
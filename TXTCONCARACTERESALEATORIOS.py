#Generar txt-------------------------------------------------------------
import random
import string

def generar_linea():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=60))

try:
    with open("file.txt", "w") as file:
        for _ in range(100):
            file.write(generar_linea() + "\n")
    print("Generado")
except:
    print("Error")
    print("Error al enviar")
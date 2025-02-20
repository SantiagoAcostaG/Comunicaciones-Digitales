#TX------------------------------------------------------
from machine import UART, Pin
import time

# Configurar UART a máxima velocidad posible
uart = UART(0, baudrate=921600, tx=Pin(0),rx=None,txbuf=4096)     

try:
    with open('file.txt', 'rb') as file:  # Nombre de archivo corregido
        content = file.read()
    
    # Enviar tamaño
    uart.write(len(content).to_bytes(4, 'big'))
    time.sleep(0.01)  # Mínimo delay necesario
    
    # Enviar contenido
    uart.write(content)
    print("Enviado")
    
except:
    print("Error")
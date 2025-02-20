#RX----------------------------------------------
from machine import UART, Pin
import time

# Configurar UART a máxima velocidad
uart = UART(0,baudrate=921600, tx=None,rx=Pin(1),rxbuf=4096)      
try:
    print("Esperando datos...")
    
    # Recibir tamaño
    while uart.any() < 4:
        time.sleep(0.001)
    size = int.from_bytes(uart.read(4), 'big')
    
    # Recibir contenido
    data = bytearray()
    while len(data) < size:
        if uart.any():
            data.extend(uart.read())
    
    # Guardar archivo
    with open('File_RX.txt', 'wb') as file:
        file.write(data)
    print("Guardado")
    
except:
    print("Error")
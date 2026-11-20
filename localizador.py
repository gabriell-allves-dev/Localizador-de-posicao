import pyautogui
import time

# Mesagem de aviso
print("Posicione o mouse...")

# Tempo de espera para posicionar o mouse
time.sleep(5)

# Guardar posição
x, y = pyautogui.position()

# Mostrar posição
print(f"X: {x} | Y: {y}")
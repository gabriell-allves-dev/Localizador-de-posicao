import pyautogui
import time

green = '\033[1;32m'
print(f'{green}')

while True:
    # Mesagem de aviso
    print("Posicione o mouse...")
    print()
    time.sleep(0.5)
    print('Espere 3 segundos')
    print()
    time.sleep(0.5)

    # Tempo de espera para posicionar o mouse
    time.sleep(3)

    # Guardar posição
    x, y = pyautogui.position()

    # Mostrar posição
    print(f"X: {x} | Y: {y}")

    # Menu de escolha
    print()
    print('[1] - Repetir novamente')
    print('[2] - Finalizar')
    print()

    opcao = int(input('Alternativa: '))
    print()

    if opcao == 1:
        continue

    elif opcao == 2:
        break

    else:
        print('Valor inválido!')
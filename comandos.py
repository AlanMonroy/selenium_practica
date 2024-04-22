import keyboard
import time

time.sleep(5)
keyboard.press('w')
time.sleep(5)
keyboard.release('w')
keyboard.press('d')
time.sleep(5)
keyboard.release('d')

"""
#Opcion 1
start = time.time()

tiempo = 0
presionado = False

while tiempo < 10:
    tiempo = time.time() - start
    print(f'Tiempo {tiempo}')

    print('Hey')"""




"""# Esperar un momento antes de simular la presión de la tecla
time.sleep(5)

# Simular la presión de la tecla "A"
pyautogui.keyDown('w')

# Mantener la tecla presionada durante 5 segundos
time.sleep(5)

# Soltar la tecla "A"
pyautogui.keyUp('w')"""

'''from pykeyboard import PyKeyboard
k = PyKeyboard()
time.sleep(5)
k.press_key('W')
time.sleep(5)
k.release_key('W')'''





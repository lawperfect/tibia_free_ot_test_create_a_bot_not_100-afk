import os
import pyautogui
from PIL import Image
import pytesseract
import pygetwindow as gw
from options import *


def status_check():
    hp_result = 0
    mp_result = 0
    # Defina as coordenadas do retângulo na tela
    left, top, width, height = pixel
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save("screenshot.png")
    text = pytesseract.image_to_string(Image.open(
        "screenshot.png"), config='--psm 6 -c tessedit_char_whitelist=0123456789')
    os.remove("screenshot.png")

    linhas = text.split("\n")
    if len(linhas) >= 2:
        hp = int(linhas[0])
        mp = int(linhas[1])
        hp_result = hp_max - hp
        mp_result = mp_max - mp
        print("HP:", hp_result)
        print("MP:", mp_result)
        return hp_result, mp_result, True  # Retorna True para indicar que é o Tibia

    else:
        print("A string não contém pelo menos duas linhas com números.")
        return 0, 0, False  # Retorna False para indicar que não é o Tibia

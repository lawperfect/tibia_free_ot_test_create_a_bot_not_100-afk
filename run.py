from check import *
from conditions import *
from options import *
import pygetwindow as gw
import pyautogui
import time
import keyboard

# Tempo de intervalo (segundos)
intervalo = 0.5

# Parte do nome da janela que você deseja encontrar (pode ser parcial)
parte_do_nome = window_name

executando = True

while executando:
    # Encontra todas as janelas com um título que contenha a "parte_do_nome"
    janelas = [j for j in gw.getAllTitles() if parte_do_nome in j]

    if janelas:
        # Foca na primeira janela encontrada
        janela = gw.getWindowsWithTitle(janelas[0])
        janela[0].activate()

    hp_result, mp_result, not_tibia = status_check()
    print("precisa de MP:", mp_result)

    if not_tibia:
        if hp_result > exura_ico:
            pyautogui.press('f')
        if mp_result > strong_mana:
            pyautogui.press('r')

    # Espera o intervalo de tempo
    time.sleep(intervalo)

    if keyboard.is_pressed('f9'):
        print("Tecla 'f9' pressionada. Parando o loop.")
        executando = False

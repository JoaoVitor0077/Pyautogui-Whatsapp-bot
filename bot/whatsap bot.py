
import pyautogui
import pyperclip
from time import sleep


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


telefones = []
with open('telefones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n'[0]))

for telefone in telefones:
    pyautogui.press('winleft')
    sleep(2)
    escrever_frase('whatsapp')
    sleep(2)
    pyautogui.press('enter')
    sleep(5)
    escrever_frase(f'{telefone}')
    sleep(5)
    pyautogui.click(698, 255, duration=1)
    sleep(5)
    # Escreva o que quer que o bot mande
    escrever_frase('')
    sleep(10)
    pyautogui.press('enter')
    sleep(10)
    pyautogui.click(1344, 77, duration=2)
    sleep(300)

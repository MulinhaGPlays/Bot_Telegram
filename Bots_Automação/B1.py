import pyautogui
import time

pyautogui.alert('Bem vindo ao B1, este BOT foi desenvolvido para automatizar algum processo desejado.')
pyautogui.keyDown('winleft')
pyautogui.press('r')
pyautogui.keyUp('winleft')
pyautogui.write("opera.exe") 
pyautogui.press('enter')
time.sleep(1.2)
pyautogui.write("https://www.github.com/MulinhaGPlays")
pyautogui.press('enter')
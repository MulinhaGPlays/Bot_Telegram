import pyautogui
import time

pyautogui.alert('Bem vindo ao B1, este BOT foi desenvolvido para automatizar algum processo desejado.')
pyautogui.PAUSE = 1
pyautogui.hotkey('winleft', 'r')
pyautogui.write("opera.exe") 
pyautogui.press('enter')
time.sleep(2)
pyautogui.write("https://www.github.com/MulinhaGPlays")
pyautogui.press('enter')
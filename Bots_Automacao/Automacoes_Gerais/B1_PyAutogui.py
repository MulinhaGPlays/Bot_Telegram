import pyautogui # Importa o PyAutoGUI para automação de interação com o usuário
import time # Importa o time para ajustar o tempo de espera

pyautogui.alert('Bem vindo ao B1, este BOT foi desenvolvido para automatizar algum processo desejado.') # Exibe um alerta na tela do usuário
pyautogui.PAUSE = 1 # Define o tempo de espera entre as interações
pyautogui.hotkey('winleft', 'r') # Abre o menu de recorte de tela do Windows
pyautogui.write("opera.exe") # Digita o nome do programa no campo de busca
pyautogui.press('enter') # Pressiona o botão de busca
time.sleep(2) # Ajusta o tempo de espera
pyautogui.write("https://www.github.com/MulinhaGPlays") # Digita o endereço do site no campo de busca
pyautogui.press('enter') # Pressiona o botão de busca
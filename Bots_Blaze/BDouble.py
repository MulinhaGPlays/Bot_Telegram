import time
import telebot
import requests
import regex as re
from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright

CHAVE_API = "5362897913:AAFkqmaFg3VJnRNYEB30yAT5EhCgGbpYNVY"
chat_id = '1970700049'

bot = telebot.TeleBot(CHAVE_API)

def send_message(text):
    bot.send_message(chat_id, text)

def send_image(file_path):
    body = {'chat_id': chat_id, }
    files = {'photo': open(file_path, 'rb')}
    r = requests.post(
        'https://api.telegram.org/bot{}/sendPhoto'.format(CHAVE_API), data=body, files=files)


send_message('Iniciando Bot...')
with sync_playwright() as playwright:
    ResultNumber = []
    ResultColor = []
    ResultHistoric = []
    RouletteNumber = []
    RouletteColor = []
    RouletteQuant = []
    chromium = playwright.chromium
    browser = chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://blaze.com/pt/games/double')
    r = 0
    send_message('Aguarde, estamos calculando os resultados...')
    while True:
        DataSite = page.content()
        soup = BeautifulSoup(DataSite, 'html.parser')
        n = -1
        if r == 0:
            for Div in soup.find_all('div', class_='sm-box'):
                n += 1
                ResultColor.append(Div['class'][1])
                ResultNumber.append(re.findall(r'\d+', Div.text))
                ResultNumber[n] = ResultNumber[n][0] if len(
                    ResultNumber[n]) > 0 else '0'
                ResultHistoric.append(
                    f'{ResultNumber[n]} {ResultColor[n]}')
            i = 0
            for a in ResultHistoric:
                i += 1
            while i != 0:
                if ResultColor[i-1] == 'red':
                    for g in range(15):
                        if f'{g}' == f'{ResultNumber[i-1]}':
                            send_image(f'Bots_Blaze/Image/Red{g}.png')
                if ResultColor[i-1] == 'black':
                    for g in range(15):
                        if f'{g}' == f'{ResultNumber[i-1]}':
                            send_image(f'Bots_Blaze/Image/Black{g}.png')
                if ResultColor[i-1] == 'white':
                    send_image('Bots_Blaze/Image/White.png')
                i = i-1
            r = 1
        elif r == 1:
            Div2 = soup.find_all('div', id='roulette', class_='page complete')
            Div1 = soup.find_all('div', class_='sm-box')[0]
            if Div2 != []:
                while Div2 == []:
                    Div2 = soup.find_all('div', id='roulette', class_='page complete')
                if Div2 != []:
                    ResultNumberT = re.findall(r'\d+', Div1.text)
                    ResultColorT = Div1['class'][1]
                    ResultHistoricT = f'{ResultNumberT[0]} {ResultColorT}'
                    ResultHistoricT = ResultHistoricT
                    if ResultColorT == 'red':
                        for g in range(15):
                            if f'{g}' == f'{ResultNumberT[0]}':
                                send_image(f'Bots_Blaze/Image/Red{g}.png')
                    if ResultColorT == 'black':
                        for g in range(15):
                            if f'{g}' == f'{ResultNumberT[0]}':
                                send_image(f'Bots_Blaze/Image/Black{g}.png')
                    if ResultColorT == 'white':
                        send_image('Bots_Blaze/Image/White.png')
                    time.sleep(8)
        
            # static
        # n = -1
        # for Div in soup.find_all('div', class_='lg-box'):
        #     n += 1
        #     RouletteColor.append(Div['class'][1])
        #     RouletteNumber.append(re.findall(r'\d+', Div.text))
        #     RouletteNumber[n] = RouletteNumber[n][0] if len(
        #         RouletteNumber[n]) > 0 else '0'
        #     RouletteQuant.append(f'{RouletteNumber[n]} {RouletteColor[n]}')
        #     send_message(RouletteQuant[n])

# outputs
# RouletteQuant
# ResultHistoric

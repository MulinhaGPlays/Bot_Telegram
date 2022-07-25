import time
import telebot
import regex as re
from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright

CHAVE_API = "5362897913:AAFkqmaFg3VJnRNYEB30yAT5EhCgGbpYNVY"
chat_id = '1970700049'

bot = telebot.TeleBot(CHAVE_API)

def send_message(text):
    bot.send_message(chat_id, text)

# with sync_playwright() as playwright:
#     resultadosNumero = []
#     resultadosCor = []
#     ResultHistoric = []
#     chromium = playwright.chromium
#     browser = chromium.launch()
#     page = browser.new_page()
#     page.goto('https://blaze.com/pt/games/double')
#     HistoricResult = page.content()
#     soup = BeautifulSoup(HistoricResult, 'html.parser')
#     n = -1
#     for resultados in soup.find_all('div', class_='sm-box'):
#         n += 1
#         resultadosCor.append(resultados['class'][1])
#         resultadosNumero.append(re.findall(r'\d+', resultados.text))
#         resultadosNumero[n] = resultadosNumero[n][0] if len(resultadosNumero[n]) > 0 else '0'
#         ResultHistoric.append(f'{resultadosNumero[n]} {resultadosCor[n]}')
#     g = -1
#     for f in ResultHistoric:
#         g += 1
#         print(ResultHistoric[g])
#         # send_message(ResultHistoric[g])
#     browser.close()

with sync_playwright() as playwright:
    resultadosNumero = []
    resultadosCor = []
    ResultHistoric = []
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto('https://blaze.com/pt/games/double')
    HistoricResult = page.content()
    soup = BeautifulSoup(HistoricResult, 'html.parser')
    n = -1
    for resultados in soup.find_all('div', class_='lg-box'):
        n += 1
        resultadosCor.append(resultados['class'][1])
        resultadosNumero.append(re.findall(r'\d+', resultados.text))
        resultadosNumero[n] = resultadosNumero[n][0] if len(resultadosNumero[n]) > 0 else '0'
        ResultHistoric.append(f'{resultadosNumero[n]} {resultadosCor[n]}')
    g = -1
    for f in ResultHistoric:
        g += 1
        print(ResultHistoric[g])
        # send_message(ResultHistoric[g])
    browser.close()
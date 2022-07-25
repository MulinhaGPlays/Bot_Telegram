import regex as re

from bs4 import BeautifulSoup


HistoricResult = '<div class="entries main"><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">11</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">14</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box white"><img alt="0" src="/static/media/logo-icon.75d9365f.svg"></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">3</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">4</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box white"><img alt="0" src="/static/media/logo-icon.75d9365f.svg"></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">10</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">12</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">6</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">5</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">9</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">6</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">8</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">2</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">7</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">2</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">11</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">4</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">9</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">8</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">14</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">10</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">6</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box black"><div class="number">10</div></div></div></div><div class="entry"><div class="roulette-tile"><div class="sm-box red"><div class="number">4</div></div></div></div></div>'
soup = BeautifulSoup(HistoricResult, 'html.parser')
resultadosNumero = []
resultadosCor = []
ResultHistoric = []

n = -1
for resultados in soup.find_all('div', class_='sm-box'):
    n += 1
    resultadosCor.append(resultados['class'][1])
    resultadosNumero.append(re.findall(r'\d+', resultados.text))
    resultadosNumero[n] = resultadosNumero[n][0] if len(
        resultadosNumero[n]) > 0 else '0'
    ResultHistoric.append(f'{resultadosNumero[n]} {resultadosCor[n]}')

g = -1
for f in ResultHistoric:
    g += 1
    print(ResultHistoric[g])

# CHAVE_API = "5362897913:AAFkqmaFg3VJnRNYEB30yAT5EhCgGbpYNVY"
# bot = telebot.TeleBot(CHAVE_API)

# def verificar(mensagem):
#     return True


# @bot.message_handler(func=verificar)
# def responder(mensagem):
#     texto = "ola"
#     bot.reply_to(mensagem, texto)


# bot.polling()

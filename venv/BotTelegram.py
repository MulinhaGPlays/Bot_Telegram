import telebot

CHAVE_API = "5362897913:AAFkqmaFg3VJnRNYEB30yAT5EhCgGbpYNVY"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem): 
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "olá")

bot.polling()
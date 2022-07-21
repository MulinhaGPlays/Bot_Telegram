import telebot # Importação do arquivo de configuração

CHAVE_API = "5362897913:AAFkqmaFg3VJnRNYEB30yAT5EhCgGbpYNVY" # Chave do bot
bot = telebot.TeleBot(CHAVE_API) # Inicialização do bot


@bot.message_handler(commands=['DizerBatata']) # Função para o comando DizerBatata
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "batata")
    
@bot.message_handler(commands=['DizerTomate']) # Função para o comando DizerTomate
def responder(mensagem):
    bot.reply_to(mensagem, "tomate") 
     
                
def verificar(mensagem): # Função para verificar se o bot foi chamado
    return True


@bot.message_handler(func=verificar) 
def responder(mensagem): # Função para responder a mensagem
    if mensagem.text == "batata?":
        texto = "sim, batata"
    else:
        texto = """Escolha um Comando:
    /DizerBatata
    /DizerTomate"""    
    bot.reply_to(mensagem, texto) # Envia a mensagem ao usuário


bot.polling() # Executa o bot
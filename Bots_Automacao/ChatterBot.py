# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# class PTGSM:
#     def __init__(self):
#         self.bot = ChatBot('Bot')
#         self.bot.set_trainer(ListTrainer)

#     def treinar(self, lista):
#         self.bot.train(lista)

#     def responder(self, pergunta):
#         return self.bot.get_response(pergunta)

#     def treinar_arquivo(self, nome_arquivo):
#         arquivo = open(nome_arquivo, 'r')
#         conversa = arquivo.readlines()
#         self.bot.train(conversa)
#         arquivo.close()
        
#     def salvar_arquivo(self, nome_arquivo):
#         arquivo = open(nome_arquivo, 'w')
#         arquivo.write(self.bot.export_for_training())
#         arquivo.close()
        
        
# PTGSM.treinar_arquivo(PTGSM, 'conversa.txt')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
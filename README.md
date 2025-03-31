# BOT TELEGRAM
*criar decorator e funcao logo em seguida*

# CHAVE API
TOKEN = "5478658940:ALSDK1932AHSDAUSDY819NCBADB8102UZB"

# CRIAR BOT
bot = telebot.TeleBot(TOKEN)

# Loop infinito - fazer o bot conversar o tempo todo com o telegram
bot.polling()

# Exemplo:
import os
import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "Bot Criado!")

bot.polling()

import os
import telebot


TOKEN = ""

# Cria o BOT
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "Bot Criado!")


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Bot Editado!")


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Bot Excluído!")


def verificar(mensagem):
    return True

# decorator e função


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
        /opcao1 Criar BOT
        /opcao2 Editar BOT
        /opcao3 Deletar BOT
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto)


# Loop infinito - fazer o bot conversar o tempo todo com o telegram
bot.polling()

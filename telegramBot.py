################
# Giovanni Gentile
# 1 November 2018
# Bot Telegram Raspberry Pi
###############

import os
import time
import telepot
import urllib

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    name = msg['from']['first_name']

    webf = urllib.urlopen('http://www.*************************.txt')
    test = webf.read()
    text = (open("text.txt", "r").read())
    orari = (open("orari.txt", "r").read())
    docenti = (open("docenti.txt", "r").read())
    riferimenti = (open("riferimenti.txt", "r").read())
    start = (open("start.txt", "r").read())
    note = (open("note.txt", "r").read())

    print('Got command: %s' % command)

    if command == '/start':
       bot.sendMessage(chat_id,'Ciao {}, il bot risponde:'.format(name))
       bot.sendMessage(chat_id, start)
    elif command =='/orari':
       bot.sendMessage(chat_id, orari)
    elif command =='/docenti':
       bot.sendMessage(chat_id, docenti)
    elif command =='/riferimenti':
       bot.sendMessage(chat_id, riferimenti)
    elif command =='/note':
       bot.sendMessage(chat_id, note)
    elif command == '/test':
       bot.sendMessage(chat_id, test)

bot = telepot.Bot('*****************************************')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')

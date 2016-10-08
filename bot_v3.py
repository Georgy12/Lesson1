from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem 

phrases={"привет":"привет","как дела":"хорошо,а у тебя","хорошо":"ну и здорово","плохо":"взбодрись"}

users_add_phrase=phrases.copy()

numbers_in_russian={'один':1,'два':2,'три':3,
'четыре':4,'пять':5,'шесть':6,'семь':7,'восемь':8,
'девять':9,'десять':10,
'умножить_на':'*','разделить_на':'/','плюс':'+','минус':'-'}

incorrect='?.,!'



def get_answer(key,phrases):
    for symbol in incorrect:
        key=key.replace(symbol,"")
    key=key.strip()
    return phrases.get(key.lower(), "")



def start(bot,update):
    print("Вызван/start")
    bot.sendMessage(update.message.chat_id, text='Привет. Напиши  /bot_help  если хочешь узнать о моём функционале.')


def bot_help(bot,update):
    print("Помощь пользователю/help")
    bot.sendMessage(update.message.chat_id, text="Список команд: /words_count  выводит количество слов,которые записаны после этой команды\n /calculate  производит математические операции с двумя числами\n"
        "/next_full_moon  сообщает дату следуещего полнолуния после указанной даты, дата указывается в формате YYYY/mm/dd\n /text_calculation производит математические действия с числами от 1 до 10,если их ввести по русски\n"
        "/add_phrase_to_dict  добавляет фразы,на которые может ответить бот,важно написать одно слово раздельно со вторым, слова в фразах должны писаться через нижнее подчеркивание")


def talk_to_me(bot,update):
    print('Получено сообщение: %s' % update.message.text)
    bot.sendMessage(update.message.chat_id, text=get_answer(update.message.text, phrases))


def talk_to_me_2(bot,update):
    print('Получено сообщение: %s' % update.message.text)
    bot.sendMessage(update.message.chat_id, text=get_answer(update.message.text,users_add_phrase))


def words_count(bot,update):
    print('Получено сообщение: %s' % update.message.text)
    words_list=update.message.text.split()
    words=len(words_list)-1
    bot.sendMessage(update.message.chat_id, text=str(words))


def calculate(bot,update):
    print('Получено сообщение: %s' % update.message.text)

    nums_for_calculation=update.message.text.strip().split()
    if "*" in nums_for_calculation:
        result=int(nums_for_calculation[1])* int(nums_for_calculation[3])
        bot.sendMessage(update.message.chat_id, text=int(result))

    if "+" in nums_for_calculation:
        result=int(nums_for_calculation[1])+ int(nums_for_calculation[3])
        bot.sendMessage(update.message.chat_id, text=int(result))


    if "-" in nums_for_calculation:
        result=int(nums_for_calculation[1])- int(nums_for_calculation[3])
        bot.sendMessage(update.message.chat_id, text=int(result))    

    if "/" in nums_for_calculation:
        if int(nums_for_calculation[3])==0:
            bot.sendMessage(update.message.chat_id, text='Нельзя делить на 0')
        else:
            result=int(nums_for_calculation[1])/ int(nums_for_calculation[3])
            bot.sendMessage(update.message.chat_id, text=int(result))    

operations = {
    "разделить на": "разделить_на",
    "умножить на":"умножить_на"
}
def text_calculation(bot,update):
    print('Получено сообщение: %s' % update.message.text)
    for op in operations:
        update.message.text = update.message.text.replace(op, operations[op])
    text_calculation_list=update.message.text.split()
    #bot.sendMessage(update.message.chat_id, text="/".join(text_calculation_list))
    first_num=numbers_in_russian.get(text_calculation_list[1])
    operation=numbers_in_russian.get(text_calculation_list[2])
    second_num=numbers_in_russian.get(text_calculation_list[3])

    if "+" in operation:
        result=int(first_num)+int(second_num)
        bot.sendMessage(update.message.chat_id, text=int(result))

    if "-" in operation:
        result=int(first_num)-int(second_num)
        bot.sendMessage(update.message.chat_id, text=int(result))

    if "*" in operation:
        result=int(first_num)*int(second_num)
        bot.sendMessage(update.message.chat_id, text=int(result))

    if "/" in operation:
        result=int(first_num)/int(second_num)
        bot.sendMessage(update.message.chat_id, text=int(result))


def next_full_moon(bot,update):
    print('Получено сообщение: %s' % update.message.text)
    ephem_list=update.message.text.split()
    date=ephem_list[1]
    bot.sendMessage(update.message.chat_id, text=str(ephem.next_full_moon(date)))


def add_phrase_to_dict(bot,update):
    print('Получено сообщение: %s' % update.message.text)
    add_phrase_list=update.message.text.split()
    users_add_phrase[str(add_phrase_list[1])]=str(add_phrase_list[2])
    bot.sendMessage(update.message.chat_id, text=str('Фраза добавлена'))
    #bot.sendMessage(update.message.chat_id, text=str(users_add_phrase))





def bot_work():
    updater=Updater("286223894:AAFR57Bru4f7xEcEBTQ4Q12pVw8SJXM0uU8")

    
    dp=updater.dispatcher 
    dp.add_handler(CommandHandler('add_phrase_to_dict',add_phrase_to_dict))
    dp.add_handler(CommandHandler('text_calculation',text_calculation))
    dp.add_handler(CommandHandler('calculate',calculate))
    dp.add_handler(CommandHandler('words_count',words_count))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('bot_help',bot_help))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me_2))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler('next_full_moon',next_full_moon))


    updater.start_polling()
    updater.idle()


if __name__==("__main__"):
    bot_work()  
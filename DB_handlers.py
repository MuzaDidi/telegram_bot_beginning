import futureBot
import DataBase
import messages


@futureBot.bot.message_handler(commands=['start'])
def send_welcome(message):
    # Если пользователя нет в базе
    if DataBase.find_users(message.chat.id) is False:
        DataBase.add_user(message)
        futureBot.bot.send_message(message.chat.id, messages.HELLO_MESSAGE, reply_markup=futureBot.shopKeyBoard)
    # Если пользователь есть в базе
    else:
        futureBot.bot.send_message(message.chat.id, messages.HELLO_AGAIN_MESSAGE, reply_markup=futureBot.shopKeyBoard)

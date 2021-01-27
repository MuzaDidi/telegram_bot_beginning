import futureBot
import DB_handlers

keyb_main = futureBot.key_board_main()


@futureBot.bot.message_handler(func=lambda message: True)
def reply_shop_menu(message):
    if message.text == "🔍 Каталог товаров":
        futureBot.bot.reply_to(message, message.text,
                               reply_markup=futureBot.keyboardMain)
    elif message.text == "🛒 Корзина":
        futureBot.bot.reply_to(message, message.text,
                               reply_markup=futureBot.shopKeyBoard)
    elif message.text == "💰 Оплата":
        futureBot.bot.reply_to(message, "Оплата/доставка info",
                               reply_markup=futureBot.shopKeyBoard)
    else:
        futureBot.bot.reply_to(message, "О нас info",
                               reply_markup=futureBot.shopKeyBoard)


@futureBot.bot.message_handler(content_types=["text"])
def any_msg(message):
    futureBot.bot.send_message(message.chat.id, "testing kb",
                               reply_markup=futureBot.keyboardMain)


@futureBot.bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    for x in keyb_main:
        if call.data == x:
            futureBot.bot.edit_message_text(chat_id=call.message.chat.id,
                                            message_id=call.message.message_id,
                                            text=x,
                                            reply_markup=futureBot.keybrd_sub(x)[1])
        elif call.data == "1" or call.data == "2" or call.data == "3":
            futureBot.bot.answer_callback_query(callback_query_id=call.id,
                                                show_alert=True,
                                                text="Вы выбрали товар")
            futureBot.bot.edit_message_text(chat_id=call.message.chat.id,
                                            message_id=call.message.message_id,
                                            text="last layer",
                                            reply_markup=futureBot.keybrd_sub(x)[0])
    if call.data == "undo":
        futureBot.bot.edit_message_text(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        text="Каталог товаров",
                                        reply_markup=futureBot.keyboardMain)


if __name__ == '__main__':
    futureBot.bot.polling(none_stop=True)

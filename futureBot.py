import telebot
import config
import DataBase


bot = telebot.TeleBot(config.TOKEN)
print(bot.get_me())
backButton = telebot.types.InlineKeyboardButton(text="back", callback_data="undo")

# создание главного меню
shopKeyBoard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_catalog = telebot.types.KeyboardButton("🔍 Каталог товаров")
btn_basket = telebot.types.KeyboardButton("🛒 Корзина")
btn_payment = telebot.types.KeyboardButton("💰 Оплата")
btn_ourInfo = telebot.types.KeyboardButton("🖌 О нас")
shopKeyBoard.add(btn_catalog, btn_basket, btn_payment, btn_ourInfo)

# создание главного каталога товаров в сообщении
keyboardMain = telebot.types.InlineKeyboardMarkup(row_width=2)


def key_board_main():

    try:
        page_main = DataBase.find_categories()
        btn_callback_reply = []

        if len(btn_callback_reply) == 0:
            for pg in page_main:
                main_men = telebot.types.InlineKeyboardButton(text=str(pg[0]), callback_data=str(pg[0]))
                keyboardMain.add(main_men)
                btn_callback_reply.append(pg[0])
        return btn_callback_reply
    except DataBase.Error as err:
        print("Error key_board_main: ", err)


def keybrd_sub(keyb_main):
    # создание ПОДкаталога товаров (товары по конкретной категории) в сообщении
    keyboard_sub1 = telebot.types.InlineKeyboardMarkup(row_width=1)
    keyboard_sub2 = telebot.types.InlineKeyboardMarkup(row_width=1)

    btn1 = telebot.types.InlineKeyboardButton(text="1t", callback_data="1")
    btn2 = telebot.types.InlineKeyboardButton(text="2t", callback_data="2")
    btn3 = telebot.types.InlineKeyboardButton(text="3t", callback_data="3")
    keyboard_sub1.add(btn1, btn2, btn3, backButton)

    page1 = DataBase.find_products(keyb_main)
    for page in page1:
        rel1 = telebot.types.InlineKeyboardButton(text=str(page[0]), callback_data=str(page[0]))
        keyboard_sub2.add(rel1)
    keyboard_sub2.add(backButton)

    keyboard_sub = [keyboard_sub1, keyboard_sub2]
    return keyboard_sub




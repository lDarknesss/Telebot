from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#кнопки клавиатуры клиента
shawa_menu = InlineKeyboardButton(text='Меню',callback_data='/Меню')
shawa_place = InlineKeyboardButton(text='Расположение',callback_data='/Расположение')
shawa_open = InlineKeyboardButton(text='Режим работы',callback_data='/Режим_работы')
shawa_order= InlineKeyboardButton(text='Заказать',callback_data='/Заказать')

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
kb_inline.insert(shawa_menu)
kb_inline.insert(shawa_place)
kb_inline.insert(shawa_open)
kb_inline.insert(shawa_order)
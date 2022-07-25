from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from database import registerCLIENT
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard import kb_inline
from database import menu



async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,'Добро пожаловать в WildBoarShaurma\nСкидка 5% после регистрации\nДля регистрации наберите /Регистрация', reply_markup=kb_inline)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напиши ему:https://t.me/WBShaurma_bot')


async def Menu(message : types.Message):
    await menu.sql_read(message)
    await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_inline)


async def place(callback : types.CallbackQuery):
    await callback.answer('Шумиловский городок, ул. Столичная 35', show_alert=True)


async def open(callback : types.CallbackQuery):
    await callback.answer('Пн-Чт: с 9.00 до 21.00, Пт-Вс: с 9.00 до 23.00', show_alert=True)


async def order(callback : types.CallbackQuery):
    await callback.answer('MTS, LIFE, A1 : +375299379992', show_alert=True)


class RegistrClient(StatesGroup):
    name = State()
    surname = State()
    email = State()
    phone = State()


#начало регистрации
@dp.message_handler(commands='Регистрация', state=None)
async def cm_start(message : types.Message):
    await RegistrClient.name.set()
    await message.reply('Назови свое имя')
#
#
# async def cancel_handler(message : types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('OK')

@dp.message_handler(state=RegistrClient.name)
async def load_name(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await RegistrClient.next()
    await message.reply('Введи свою фамилию')

@dp.message_handler(state=RegistrClient.surname)
async def load_surname(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await RegistrClient.next()
    await message.reply('Введи свою электронную почту')

@dp.message_handler(state=RegistrClient.email)
async def email(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await RegistrClient.next()
    await message.reply('Введи свой номер')

@dp.message_handler(state=RegistrClient.phone)
async def phone(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await registerCLIENT.sql_add_command(state)  # add db
    await state.finish()  # выход из состояний


#регистрация хендлеров
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_callback_query_handler(Menu, text='/Меню')
    dp.register_callback_query_handler(place, text='/Расположение')
    dp.register_callback_query_handler(open, text='/Режим_работы')
    dp.register_callback_query_handler(order, text='/Заказать')
    # dp.register_message_handler(cm_start, commands=['/Регистрация'], state=None)
    # dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    # dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    # dp.register_message_handler(load_name, content_types=['name'], state=RegistrClient.name)
    # dp.register_message_handler(load_surname, state=RegistrClient.surname)
    # dp.register_message_handler(email, state=RegistrClient.email)
    # dp.register_message_handler(phone, state=RegistrClient.phone)








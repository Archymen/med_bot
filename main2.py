import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import time



from translator import *

from config import *


name = 'Выбери исполнителя'


API_TOKEN = '5836607163:AAGGss8VBv-8YgWO1Q4y6tiF0bAiFYmVGqY'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id="-1001506876131", user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Начать", callback_data="go"))
        await message.answer(f"Привет будущий доктор, дабы облегчить твое обучение в\nмедицинском, мы создали этого бота и надеемся что он будет тебе полезен", reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Подписаться", url='https://t.me/TEAMRMC'))
        await bot.send_message(message.from_user.id, (f"Привет {message.from_user.first_name} \nДля того, чтобы пользоваться ботом,\nнеобходимо подписаться на наш канал RMC и снова нажать на\n/start, этот бот сделан для того, чтобы\nты мог разобраться с непонятными\nтемами в учебе или найти себе исполнителя\nдля работы"),reply_markup=keyboard)




@dp.callback_query_handler(text="go")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Переводчик", callback_data="translator"))
    keyboard.add(types.InlineKeyboardButton(text="Стомат", callback_data="stomat"))
    keyboard.add(types.InlineKeyboardButton(text="Леч фак", callback_data="lech_fak"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с экзаменами", callback_data="exams_help"))
    keyboard.add(types.InlineKeyboardButton(text="Для ленивых", callback_data="other"))
    keyboard.add(types.InlineKeyboardButton(text="Информация", callback_data="info"))
    await call.message.answer("Выбери факультет", reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="info")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="go"))
    await call.message.answer("Команда RMC создала для вас бота, который поможет облегчить ваше обучение в медицинском универе\nНадеемся что данный бот будет вам полезен и оставит лишь положительные эмоции\nНиже ссылки на наши основные сайты\n\nhttps://vk.com/rmc2020 наша группа ВКонтакте\n\nhttps://t.me/TEAMRMC наш канал в тг\n\nhttps://vk.me/join/AJQ1dyA2WBqtl0yxXIZOj6KF беседа на общий чат мед-вузов страны", reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="other")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Презентации", callback_data="presentation"))
    keyboard.add(types.InlineKeyboardButton(text="Конспекты", callback_data="konspekt"))
    keyboard.add(types.InlineKeyboardButton(text="Рефераты", callback_data="referat"))
    keyboard.add(types.InlineKeyboardButton(text="Доклады", callback_data="doclad"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="go"))
    await call.message.answer("Выбери курс", reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="1", callback_data="course_1"))
    keyboard.add(types.InlineKeyboardButton(text="2", callback_data="stomat_2"))
    keyboard.add(types.InlineKeyboardButton(text="3", callback_data="stomat_3"))
    keyboard.add(types.InlineKeyboardButton(text="4", callback_data="stomat_4"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="go"))
    await call.message.answer("Выбери курс", reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="lech_fak")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="1", callback_data="lech_fak_1"))
    keyboard.add(types.InlineKeyboardButton(text="2", callback_data="lech_fak_2"))
    keyboard.add(types.InlineKeyboardButton(text="3", callback_data="lech_fak_3"))
    keyboard.add(types.InlineKeyboardButton(text="4", callback_data="lech_fak_4"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="go"))
    await call.message.answer("Выбери курс", reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="course_1")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Анатомия", callback_data="stomat_1_anatomia"))
    keyboard.add(types.InlineKeyboardButton(text="Пропедевтика стомат", callback_data="stomat_1_propovedika_stomat"))
    keyboard.add(types.InlineKeyboardButton(text="Английский", callback_data="stomat_1_english"))
    keyboard.add(types.InlineKeyboardButton(text="Биология", callback_data="stomat_1_biology"))
    keyboard.add(types.InlineKeyboardButton(text="БХ", callback_data="stomat_1_BX"))
    keyboard.add(types.InlineKeyboardButton(text="Гистология", callback_data="stomat_1_hystology"))
    keyboard.add(types.InlineKeyboardButton(text="Информатика", callback_data="stomat_1_informatika"))
    keyboard.add(types.InlineKeyboardButton(text="История медицины", callback_data="stomat_1_med_history"))
    keyboard.add(types.InlineKeyboardButton(text="История России", callback_data="stomat_1_rus_history"))
    keyboard.add(types.InlineKeyboardButton(text="Латынь", callback_data="stomat_1_latin"))
    keyboard.add(types.InlineKeyboardButton(text="Физиология", callback_data="stomat_1_physyology"))
    keyboard.add(types.InlineKeyboardButton(text="Физика", callback_data="stomat_1_physic"))
    keyboard.add(types.InlineKeyboardButton(text="Химия", callback_data="stomat_1_chemistry"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_2")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="БЖД", callback_data="stomat_2_BZHD"))
    keyboard.add(types.InlineKeyboardButton(text="БХ", callback_data="stomat_2_BX"))
    keyboard.add(types.InlineKeyboardButton(text="Пропедевтика стомат", callback_data="stomat_2_propovedika_stomat"))
    keyboard.add(types.InlineKeyboardButton(text="История России", callback_data="stomat_2_rus_history"))
    keyboard.add(types.InlineKeyboardButton(text="История медицины", callback_data="stomat_2_med_history"))
    keyboard.add(types.InlineKeyboardButton(text="ОЗПТ", callback_data="stomat_2_ozpt"))
    keyboard.add(types.InlineKeyboardButton(text="Латынь", callback_data="stomat_2_latin"))
    keyboard.add(types.InlineKeyboardButton(text="Микробиология", callback_data="stomat_2_microbiology"))
    keyboard.add(types.InlineKeyboardButton(text="ЦСТ", callback_data="stomat_2_cst"))
    keyboard.add(types.InlineKeyboardButton(text="Патан", callback_data="stomat_2_patan"))
    keyboard.add(types.InlineKeyboardButton(text="Патфиз", callback_data="stomat_2_patfiz"))
    keyboard.add(types.InlineKeyboardButton(text="Профилактика", callback_data="stomat_2_profilaktika"))
    keyboard.add(types.InlineKeyboardButton(text="Физиология", callback_data="stomat_2_physyology"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_3")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Фармакология", callback_data="stomat_3_pharma"))
    keyboard.add(types.InlineKeyboardButton(text="Простое зубопротезирование", callback_data="stomat_3_prostoe_zuboprotezirovanie"))
    keyboard.add(types.InlineKeyboardButton(text="Местное обезбаливание", callback_data="stomat_3_mestnoe_obezbalivanie"))
    keyboard.add(types.InlineKeyboardButton(text="Эндодонтия", callback_data="stomat_3_endodontiya"))
    keyboard.add(types.InlineKeyboardButton(text="Кариесология", callback_data="stomat_3_kariesology"))
    keyboard.add(types.InlineKeyboardButton(text="Внутренние болезни", callback_data="stomat_3_vnutrennye"))
    keyboard.add(types.InlineKeyboardButton(text="Хирургические болезни", callback_data="stomat_3_xirurgycheskiye"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_4")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Неврология", callback_data="stomat_4_nevrology"))
    keyboard.add(types.InlineKeyboardButton(text="Эндодонтия", callback_data="stomat_4_endodontiya"))
    keyboard.add(types.InlineKeyboardButton(text="Кариесология", callback_data="stomat_4_kariesology"))
    keyboard.add(types.InlineKeyboardButton(text="Внутренние болезни", callback_data="stomat_4_vnutrennye"))
    keyboard.add(types.InlineKeyboardButton(text="Хирургические болезни", callback_data="stomat_4_xirurgycheskiye"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_1")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Анатомия", callback_data="lech_fak_1_anatomia"))
    keyboard.add(types.InlineKeyboardButton(text="Английский", callback_data="lech_fak_1_english"))
    keyboard.add(types.InlineKeyboardButton(text="Биология", callback_data="lech_fak_1_biology"))
    keyboard.add(types.InlineKeyboardButton(text="Гистология", callback_data="lech_fak_1_hystology"))
    keyboard.add(types.InlineKeyboardButton(text="Информатика", callback_data="lech_fak_1_informatika"))
    keyboard.add(types.InlineKeyboardButton(text="История медицины", callback_data="lech_fak_1_med_history"))
    keyboard.add(types.InlineKeyboardButton(text="История России", callback_data="lech_fak_1_rus_history"))
    keyboard.add(types.InlineKeyboardButton(text="Латынь", callback_data="lech_fak_1_latin"))
    keyboard.add(types.InlineKeyboardButton(text="Физика", callback_data="lech_fak_1_physic"))
    keyboard.add(types.InlineKeyboardButton(text="Химия", callback_data="lech_fak_1_chemistry"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_2")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="БЖД", callback_data="lech_fak_2_BZHD"))
    keyboard.add(types.InlineKeyboardButton(text="БХ", callback_data="lech_fak_2_BX"))
    keyboard.add(types.InlineKeyboardButton(text="История России", callback_data="lech_fak_2_rus_history"))
    keyboard.add(types.InlineKeyboardButton(text="Латынь", callback_data="lech_fak_2_latin"))
    keyboard.add(types.InlineKeyboardButton(text="Микробиология", callback_data="lech_fak_2_microbiology"))
    keyboard.add(types.InlineKeyboardButton(text="Патан", callback_data="lech_fak_2_patan"))
    keyboard.add(types.InlineKeyboardButton(text="Гистология", callback_data="lech_fak_2_hystology"))
    keyboard.add(types.InlineKeyboardButton(text="Патфиз", callback_data="lech_fak_2_patfiz"))
    keyboard.add(types.InlineKeyboardButton(text="Физиология", callback_data="lech_fak_2_physyology"))
    keyboard.add(types.InlineKeyboardButton(text="Топ Анат", callback_data="lech_fak_2_top_anat"))
    keyboard.add(types.InlineKeyboardButton(text="Оперативная хирургия", callback_data="lech_fak_2_operativnaya_xirurgiya"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()




@dp.callback_query_handler(text="lech_fak_3")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Патан", callback_data="lech_fak_3_patan"))
    keyboard.add(types.InlineKeyboardButton(text="Патфиз", callback_data="lech_fak_3_patfiz"))
    keyboard.add(types.InlineKeyboardButton(text="Фарма", callback_data="lech_fak_3_pharma"))
    keyboard.add(types.InlineKeyboardButton(text="Пропед леч", callback_data="lech_fak_3_proped_lech"))
    keyboard.add(types.InlineKeyboardButton(text="Топ Анат", callback_data="lech_fak_3_top_anat"))
    keyboard.add(types.InlineKeyboardButton(text="БХ", callback_data="lech_fak_3_bx"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="lech_fak_4")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Неврология", callback_data="lech_fak_4_nevrology"))
    keyboard.add(types.InlineKeyboardButton(text="Терапия", callback_data="lech_fak_4_terapy"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak"))
    await call.message.answer('Выбери предмет', reply_markup=keyboard)
    await call.message.delete()





@dp.callback_query_handler(text="stomat_1_anatomia")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_anatomia_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_anatomia_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_1_anatomia_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_1_anatomia_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_anatomia"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in course_1_stomat_anatomia_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_anatomia_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_anatomia"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in course_1_stomat_anatomia_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_anatomia_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_anatomia"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_anatomia_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_propovedika_stomat")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Заполнение альбомов и рт", callback_data="stomat_1_propovedika_stomat_zapolnenie_albomov_i_rt"))
    keyboard.add(types.InlineKeyboardButton(text="Лепка зубов", callback_data="stomat_1_propovedika_stomat_lepka_zubov"))
    keyboard.add(types.InlineKeyboardButton(text="Продажа стоматологических материалов", callback_data="stomat_1_propovedika_prodazha_stom_materiala"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_propovedika_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="stomat_1_propovedika_stomat_zapolnenie_albomov_i_rt")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_propovedika_stomat_zapolnenie_albomov_i_rt:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_propovedika_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_propovedika_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_propovedika_stomat_lepka_zubov")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_propovedika_stomat_lepka_zubov:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_propovedika_prodazha_stom_materiala")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_propovedika_prodazha_stom_materiala:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_english")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_english_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_english_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="stomat_1_english_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_1_english_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_english"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_english_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_english_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_english"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_english_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_english_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_english"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_english_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_biology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_biology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_biology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Заполнение рт", callback_data="stomat_1_biology_zapolnenie_rt"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_1_biology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_biology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_biology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_biology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_biology_zapolnenie_rt")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_biology_zapolnenie_rt:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_BX")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_BX_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_BX_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="stomat_1_BX_help"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_1_BX_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="stomat_1_BX_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_BX_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="stomat_1_BX_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_BX_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_BX_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_BX_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_BX_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_BX_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="stomat_1_hystology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_hystology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_hystology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_1_hystology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_hystology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_hystology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_hystology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_hystology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_hystology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_informatika")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_informatika_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Изготовление итоговых работ", callback_data="stomat_1_informatika_final_works"))
    keyboard.add(types.InlineKeyboardButton(text="Домашнее задание", callback_data="stomat_1_informatika_dz"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_informatika_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_informatika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_informatika_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_informatika_final_works")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_informatika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_informatika_final_works:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_informatika_dz")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_informatika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_informatika_dz:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_med_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_med_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_med_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_med_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_med_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_1_rus_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_rus_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_rus_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_rus_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_rus_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_latin")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_latin_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_latin_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="stomat_1_latin_help"))
    keyboard.add(types.InlineKeyboardButton(text="Домашнее задание", callback_data="stomat_1_latin_dz"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_latin_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_latin_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_latin_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_latin_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_latin_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_latin_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_latin_dz")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_latin_dz:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_physyology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_physyology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_physyology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_physyology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_physyology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_physic")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_physic_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_physic_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_physic"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_physic_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_1_chemistry")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_1_chemistry_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_1_chemistry_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="course_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_1_chemistry_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_chemistry"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_chemistry_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_1_chemistry_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_1_chemistry"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_1_chemistry_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_anatomia")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_1_anatomia_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_anatomia_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_1_anatomia_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_1_anatomia_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_anatomia"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_anatomia_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_anatomia_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_anatomia"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_anatomia_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_anatomia_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_anatomia"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_anatomia_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="lech_fak_1_english")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_1_english_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_english_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_1_english_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="lech_fak_1_english_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_english"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_english_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="lech_fak_1_english_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_english"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_english_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_english_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_english"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_english_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_biology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_1_biology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_biology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Заполнение рт", callback_data="lech_fak_1_biology_zapolnenie_rt"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_1_biology_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_1_biology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_biology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_biology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_biology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_biology_zapolnenie_rt")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_biology_zapolnenie_rt:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_biology_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_biology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_biology_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_hystology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_1_hystology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_hystology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_1_hystology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_hystology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_hystology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_hystology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_hystology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_hystology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="lech_fak_2_hystology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_hystology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_2_hystology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_2_hystology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_hystology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_hystology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_hystology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_hystology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_hystology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_2_top_anat")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_top_anat_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_2_top_anat_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()




@dp.callback_query_handler(text="lech_fak_2_top_anat_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_top_anat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_top_anat_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_top_anat_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_top_anat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_top_anat_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)









@dp.callback_query_handler(text="lech_fak_2_operativnaya_xirurgiya")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_2_operativnaya_xirurgiya_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_2_operativnaya_xirurgiya_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_operativnaya_xirurgiya"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_operativnaya_xirurgiya_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)








@dp.callback_query_handler(text="lech_fak_1_informatika")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_informatika_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Изготовление итоговых работ", callback_data="lech_fak_1_informatika_final_works"))
    keyboard.add(types.InlineKeyboardButton(text="Заполнение рт", callback_data="lech_fak_1_informatika_dz"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_1_informatika_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_informatika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_informatika_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_informatika_final_works")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_informatika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_informatika_final_works:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_1_informatika_dz")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_informatika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_informatika_dz:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_1_med_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_med_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()




@dp.callback_query_handler(text="lech_fak_1_med_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_med_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_med_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_rus_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_rus_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_1_rus_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_rus_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_rus_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_latin")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_1_latin_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_latin_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Домашнее задание", callback_data="lech_fak_1_latin_dz"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_1_latin_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_1_latin_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_latin_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_latin_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_latin_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_latin_dz")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_latin_dz:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_latin_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_latin_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_chemistry")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_1_chemistry_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_chemistry_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_1_chemistry_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="lech_fak_1_chemistry_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_chemistry"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_chemistry_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_chemistry_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_chemistry"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_chemistry_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_1_chemistry_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_chemistry"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_chemistry_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_1_physic")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_1_physic_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_1_physic_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_1_physic"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_1_physic_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_BZHD")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_BZHD_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_BZHD_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_BZHD"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_BZHD_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_ozpt")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Практика", callback_data="stomat_2_ozpt_praktike"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_2_ozpt_praktike")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_ozpt"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_ozpt_praktike:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="stomat_2_BX")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_2_BX_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_BX_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="stomat_2_BX_help"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_BX_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="stomat_2_BX_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_BX_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="stomat_2_BX_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_BX_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_BX_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_BX_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_BX_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_BX_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_rus_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_rus_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_rus_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_rus_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_rus_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="stomat_2_med_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_med_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_med_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_med_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_rus_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_latin")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_2_latin_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="stomat_2_latin_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_latin_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_latin_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_latin_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_latin_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_profilaktika")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_profilaktika_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_2_profilaktika_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_profilaktika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_profilaktika_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="stomat_2_microbiology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_2_microbiology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_microbiology_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="stomat_2_microbiology_help"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_microbiology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="stomat_2_microbiology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_microbiology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_microbiology_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_microbiology_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_microbiology_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_microbiology_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_microbiology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_microbiology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="stomat_2_patan")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_2_patan_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_patan_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_2_patan_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_patan"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_patan_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_patan_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_patan"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_patan_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="stomat_2_patfiz")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_2_patfiz_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_patfiz_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_patfiz_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_2_patfiz_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_patfiz_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_patfiz_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_patfiz_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)










@dp.callback_query_handler(text="stomat_2_patfiz_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_patfiz_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="stomat_2_physyology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_2_physyology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестоов", callback_data="stomat_2_physyology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_physyology_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_physyology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_physyology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_physyology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_physyology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_physyology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_physyology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)







@dp.callback_query_handler(text="stomat_2_physyology_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_physyology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_physyology_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_2_BZHD")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_2_BZHD_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_2_BZHD_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_BZHD"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_BZHD_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_BX")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_BX_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестоов", callback_data="lech_fak_2_BX_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_2_BX_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_2_BX_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_BX_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_BX_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_BX_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="lech_fak_2_BX_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_BX"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_BX_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_2_rus_history")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_2_rus_history_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_2_rus_history_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_rus_history"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_rus_history_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_latin")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_latin_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_2_latin_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_2_latin_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_latin_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_latin_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_latin"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_latin_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_microbiology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_microbiology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_2_microbiology_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_2_microbiology_help"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_2_microbiology_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_2_microbiology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_microbiology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="lech_fak_2_microbiology_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_microbiology_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)







@dp.callback_query_handler(text="lech_fak_2_microbiology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_microbiology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_microbiology_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_microbiology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_microbiology_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_patfiz")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_patfiz_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_2_patfiz_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_2_patfiz_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="lech_fak_2_patfiz_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_patfiz_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_2_patfiz_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_patfiz_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="lech_fak_2_patfiz_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_patfiz_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_physyology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_2_physyology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_2_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_2_physyology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_physyology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_physyology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_2_physyology_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_2_physyology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_2_physyology_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_3_bx")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_3_bx_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_3_bx_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_3_bx_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Помощь с контрольными", callback_data="lech_fak_3_bx_help"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_3_bx_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_bx"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_bx_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_3_bx_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_bx"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_bx_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_3_bx_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_bx"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_bx_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="lech_fak_3_bx_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_bx"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_bx_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)










@dp.callback_query_handler(text="lech_fak_3_top_anat")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_3_top_anat_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_3_top_anat_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()




@dp.callback_query_handler(text="lech_fak_3_top_anat_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_top_anat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_top_anat_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_3_top_anat_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_top_anat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_top_anat_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)








@dp.callback_query_handler(text="lech_fak_3_patfiz")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_3_patfiz_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_3_patfiz_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_3_patfiz_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()





@dp.callback_query_handler(text="lech_fak_3_patfiz_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_patfiz_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_3_patfiz_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_patfiz_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_3_patfiz_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_patfiz"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_patfiz_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_3_pharma")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_3_pharma_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="lech_fak_3_pharma_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_3_pharma_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_3_pharma_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_pharma"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_pharma_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="lech_fak_3_pharma_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_pharma"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_pharma_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="lech_fak_3_pharma_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_pharma"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_pharma_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_3_proped_lech")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Написание ИБ", callback_data="lech_fak_3_proped_lech_ib"))
    keyboard.add(types.InlineKeyboardButton(text="Расшифровка анализов", callback_data="lech_fak_3_proped_lech_analiz"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_3_proped_lech_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_3_proped_lech_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="lech_fak_3_proped_lech_ib")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_proped_lech"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_proped_lech_ib:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_3_proped_lech_analiz")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_proped_lech"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_proped_lech_analiz:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_3_proped_lech_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_proped_lech"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_proped_lech_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="lech_fak_3_proped_lech_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_proped_lech"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_proped_lech_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)







@dp.callback_query_handler(text="lech_fak_3_patan")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_3_patan_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_3_patan_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_3_patan"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_3_patan_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="stomat_3_pharma")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_3_pharma_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_3_pharma_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_pharma"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_pharma_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_3_kariesology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_3_kariesology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_3_kariesology_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="stomat_3_kariesology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_kariesology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_kariesology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_3_kariesology_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_kariesology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_kariesology_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_3_vnutrennye")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_3_vnutrennye_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_3_vnutrennye_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_3_vnutrennye_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_vnutrennye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_vnutrennye_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_3_vnutrennye_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_vnutrennye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_vnutrennye_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_3_xirurgycheskiye")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_3_xirurgycheskiye_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_3_xirurgycheskiye_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_3_xirurgycheskiye_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_xirurgycheskiye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_xirurgycheskiye_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_3_xirurgycheskiye_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_xirurgycheskiye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_xirurgycheskiye_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)








@dp.callback_query_handler(text="stomat_3_endodontiya")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_3_endodontiya_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_3_endodontiya_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_3_endodontiya_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_endodontiya"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_endodontiya_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_3_endodontiya_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_endodontiya"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_endodontiya_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="stomat_3_mestnoe_obezbalivamie")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_3_mestnoe_obezbalivamie_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_3_mestnoe_obezbalivamie_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_mestnoe_obezbalivamie"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_mestnoe_obezbalivamie_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)








@dp.callback_query_handler(text="stomat_3_prostoe_zuboprotezirovanie")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_3_prostoe_zuboprotezirovanie_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_3_prostoe_zuboprotezirovanie_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_3_prostoe_zuboprotezirovanie"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_3_prostoe_zuboprotezirovanie_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)








@dp.callback_query_handler(text="stomat_4_kariesology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_4_kariesology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_4_kariesology_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()



@dp.callback_query_handler(text="stomat_4_kariesology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_kariesology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_kariesology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_4_kariesology_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_kariesology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_kariesology_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_4_vnutrennye")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_4_vnutrennye_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_4_vnutrennye_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_4_vnutrennye_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_vnutrennye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_vnutrennye_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_4_vnutrennye_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_vnutrennye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_vnutrennye_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_4_xirurgycheskiye")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_4_xirurgycheskiye_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_4_xirurgycheskiye_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_4_xirurgycheskiye_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_xirurgycheskiye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_xirurgycheskiye_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_4_xirurgycheskiye_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_xirurgycheskiye"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_xirurgycheskiye_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)
















@dp.callback_query_handler(text="stomat_4_nevrology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_4_nevrology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_4_nevrology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_nevrology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_nevrology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_4_endodontiya")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="stomat_4_endodontiya_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_4_endodontiya_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()




@dp.callback_query_handler(text="stomat_4_endodontiya_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_4_endodontiya"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_4_endodontiya_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)




@dp.callback_query_handler(text="lech_fak_4_nevrology")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_4_nevrology_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="lech_fak_4_nevrology_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_4_nevrology"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_4_nevrology_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="lech_fak_4_terapy")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Репетиторство", callback_data="lech_fak_4_terapy_tutoring"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="lech_fak_4_terapy_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_4"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="lech_fak_4_terapy_tutoring")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_4_terapy"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_4_terapy_tutoring:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)

@dp.callback_query_handler(text="lech_fak_4_terapy_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="lech_fak_4_terapy"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in lech_fak_4_terapy_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)





@dp.callback_query_handler(text="stomat_2_cst")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Домашнее задание", callback_data="stomat_2_cst_dz"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_cst_dz")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_cst"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_cst_dz:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_profillaktika")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Памятки", callback_data="stomat_2_profillaktika_pamyatki"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()

@dp.callback_query_handler(text="stomat_2_profillaktika_pamyatki")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_profillaktika"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_profillaktika_pamyatki:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)










@dp.callback_query_handler(text="presentation")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="other"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in presentation:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="konspekt")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="other"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in konspekt:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="referat")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="other"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in referat:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="doclad")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="other"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in doclad:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_propovedika_stomat")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Заполнение альбомов и рт", callback_data="stomat_2_propovedika_stomat_zapolnenie_albomov_i_rt"))
    keyboard.add(types.InlineKeyboardButton(text="Лепка зубов", callback_data="stomat_2_propovedika_stomat_lepka_zubov"))
    keyboard.add(types.InlineKeyboardButton(text="Продажа стоматологических материалов", callback_data="stomat_2_propovedika_prodazha_stom_materiala"))
    keyboard.add(types.InlineKeyboardButton(text="Решение тестов", callback_data="stomat_2_propovedika_solving_tests"))
    keyboard.add(types.InlineKeyboardButton(text="Диктовка", callback_data="stomat_2_propovedika_diktovka"))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2"))
    await call.message.answer('Выбери услугу', reply_markup=keyboard)
    await call.message.delete()


@dp.callback_query_handler(text="stomat_2_propovedika_solving_tests")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_propovedika_solving_tests:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_propovedika_diktovka")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_propovedika_diktovka:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






@dp.callback_query_handler(text="stomat_2_propovedika_stomat_zapolnenie_albomov_i_rt")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_propovedika_stomat_zapolnenie_albomov_i_rt:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="stomat_2_propovedika_stomat_lepka_zubov")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_propovedika_stomat_lepka_zubov:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)


@dp.callback_query_handler(text="stomat_2_propovedika_prodazha_stom_materiala")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="stomat_2_propovedika_stomat"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in stomat_2_propovedika_prodazha_stom_materiala:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)



@dp.callback_query_handler(text="exams_help")
async def process_start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="go"))
    keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/start"]
    keyboard_2.add(*buttons)
    for i in exams_help:
        await bot.send_message(message.from_user.id, i, reply_markup=keyboard_2)
        time.sleep(0.2)
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, name, reply_markup=keyboard)






















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

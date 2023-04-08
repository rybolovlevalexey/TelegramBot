from aiogram import Bot, Dispatcher, F
# класс бота, диспетчер обрабатывающий сообщения, класс с типом приходящего контента
from aiogram.types import Message, ContentType
# сообщение, класс с подготовленными возможными типами
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# создание клавы, создание кнопок клавы, удаление кнопок клавы
from aiogram.filters import Command, CommandStart, Text
# тип для фильтра - пришедшее сообщение команда(/....), команда старт, текст
from aiogram.utils.keyboard import ReplyKeyboardBuilder
# класс кнопки расширенный методами по манипуляции

btn1: KeyboardButton = KeyboardButton(text="да")
btn2: KeyboardButton = KeyboardButton(text="нет")
file = open("service information.txt")
bot = Bot(token=file.readline().split()[1])
dp: Dispatcher = Dispatcher()
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[btn1, btn2]],
                                                    resize_keyboard=True)

async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def send_no_kill_markup(message: Message):
    await message.answer("Ясно, понятно", reply_markup=ReplyKeyboardRemove())

async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь',
                         reply_markup=keyboard)

async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

async def send_echo(message: Message):
    await message.answer(message.text)

async def send_doument(message: Message):
    await message.answer("Прислан документ на обработку")
    data = message.json()

async def send_sticker(message: Message):
    await message.answer("Прислан стикер")
    await message.reply_sticker(message.sticker.file_id)

# в диспетчере указывается, на какие сообщения, как реагировать
dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_no_kill_markup, Text(text="нет"))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_doument, F.content_type == ContentType.DOCUMENT)
dp.message.register(send_sticker, F.content_type == ContentType.STICKER)
dp.message.register(send_echo)  # в самом конце, потому что ловит абсолютно любые сообщения
if __name__ == "__main__":
    dp.run_polling(bot)